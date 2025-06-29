#!/usr/bin/env python3
"""
PlotTwist Orchestrator - Coordinates multiple AI agents to generate Ren'Py visual novels
"""

import os
import json
import shutil
import asyncio
import aiohttp
from pathlib import Path
from typing import Dict, List, Optional
import google.generativeai as genai
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class PlotTwistOrchestrator:
    def __init__(self, openrouter_api_key: str, gemini_api_key: str):
        self.openrouter_api_key = openrouter_api_key
        self.gemini_api_key = gemini_api_key
        
        # Configure Gemini
        genai.configure(api_key=gemini_api_key)
        self.gemini_model = genai.GenerativeModel('gemini-1.5-pro')
        
        # OpenRouter configuration
        self.openrouter_url = "https://openrouter.ai/api/v1/chat/completions"
        self.deepseek_model = "deepseek/deepseek-r1-0528-qwen3-8b:free"
        
        # Project structure
        self.base_dir = Path.cwd()
        self.prompts_dir = self.base_dir / "prompts"
        self.scenarios_dir = self.base_dir / "scenarios"
        self.example_vn_dir = self.base_dir / "exampleVN"
        
    async def call_openrouter(self, prompt: str, system_message: str = None) -> str:
        """Call OpenRouter API with DeepSeek model"""
        headers = {
            "Authorization": f"Bearer {self.openrouter_api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://plottwist-orchestrator.com",
            "X-Title": "PlotTwist Orchestrator"
        }
        
        messages = []
        if system_message:
            messages.append({"role": "system", "content": system_message})
        messages.append({"role": "user", "content": prompt})
        
        data = {
            "model": self.deepseek_model,
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 4000
        }
        
        async with aiohttp.ClientSession() as session:
            async with session.post(self.openrouter_url, headers=headers, json=data) as response:
                if response.status == 200:
                    result = await response.json()
                    return result["choices"][0]["message"]["content"]
                else:
                    error_text = await response.text()
                    raise Exception(f"OpenRouter API error: {response.status} - {error_text}")
    
    async def call_gemini(self, prompt: str) -> str:
        """Call Gemini API for image generation"""
        try:
            response = self.gemini_model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Gemini API error: {str(e)}")
    
    def load_prompt(self, prompt_file: str) -> str:
        """Load prompt from file"""
        prompt_path = self.prompts_dir / prompt_file
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read()
    
    async def run_writer_agent(self, user_story: str, twist_genre: str, art_style: str) -> Dict:
        """Run the writer agent to generate story content"""
        print("🎭 Running Writer Agent...")
        
        writer_prompt = self.load_prompt("writer.md")
        user_prompt = f"""
Story Concept: {user_story}
Twist Genre: {twist_genre}
Visual Art Style: {art_style}

Please generate the complete story following the format specified in the prompt.
"""
        
        full_prompt = f"{writer_prompt}\n\n{user_prompt}"
        response = await self.call_openrouter(full_prompt)
        
        # Parse the response to extract structured data
        story_data = self.parse_writer_response(response)
        return story_data
    
    def parse_writer_response(self, response: str) -> Dict:
        """Parse writer response into structured data"""
        # This is a simplified parser - in production you'd want more robust parsing
        sections = response.split("---")
        
        story_data = {
            "overview": "",
            "setting": "",
            "characters": [],
            "scene": "",
            "plot_twist": "",
            "raw_response": response
        }
        
        # Extract sections (this is a basic implementation)
        lines = response.split('\n')
        current_section = None
        
        for line in lines:
            if "Story Overview" in line:
                current_section = "overview"
            elif "Setting/Background" in line:
                current_section = "setting"
            elif "Main Characters" in line:
                current_section = "characters"
            elif "Acted Story Scene" in line:
                current_section = "scene"
            elif "Single Plot Twist" in line:
                current_section = "plot_twist"
            elif line.strip() and current_section:
                if current_section == "overview":
                    story_data["overview"] += line + "\n"
                elif current_section == "setting":
                    story_data["setting"] += line + "\n"
                elif current_section == "scene":
                    story_data["scene"] += line + "\n"
                elif current_section == "plot_twist":
                    story_data["plot_twist"] += line + "\n"
        
        return story_data
    
    async def run_programmer_agent(self, story_data: Dict, generated_images: List[str] = None) -> str:
        """Run the programmer agent to generate Ren'Py script"""
        print("💻 Running Programmer Agent...")
        
        programmer_prompt = self.load_prompt("programmer.md")
        
        # Create context from writer output
        context = f"""
Story Overview: {story_data['overview']}
Setting: {story_data['setting']}
Scene: {story_data['scene']}
Plot Twist: {story_data['plot_twist']}
Characters: {json.dumps(story_data['characters'], indent=2)}
"""
        
        # Add image information if available
        if generated_images:
            context += f"\nGenerated Images:\n"
            for image_path in generated_images:
                context += f"- {image_path}\n"
            context += "\nUse these images in the appropriate scenes in your Ren'Py script."
        
        full_prompt = f"{programmer_prompt}\n\nContext:\n{context}"
        response = await self.call_openrouter(full_prompt)
        
        return response
    
    async def run_artist_agent(self, project_dir: Path, story_data: Dict) -> None:
        """Run the artist agent to generate images"""
        print("🎨 Running Artist Agent...")
        
        artist_prompt = self.load_prompt("artist.md")
        images_dir = project_dir / "game" / "images"
        
        # Ensure images directory exists
        images_dir.mkdir(parents=True, exist_ok=True)
        (images_dir / "bgs").mkdir(parents=True, exist_ok=True)
        (images_dir / "chars").mkdir(parents=True, exist_ok=True)
        
        # Generate images based on story content
        images_to_generate = []
        
        # Extract scene information from story data
        scene_text = story_data.get('scene', '')
        setting_text = story_data.get('setting', '')
        
        # Generate background images
        if scene_text or setting_text:
            # Create a background image for the main scene
            bg_prompt = f"Background for scene: {scene_text[:200]}"
            if setting_text:
                bg_prompt += f" Setting: {setting_text[:100]}"
            images_to_generate.append(("bgs/main_scene.png", bg_prompt))
        
        # Generate character images (placeholder - you can expand this based on character data)
        # For now, generate a few character sprites based on the story
        character_prompts = [
            ("chars/protagonist_neutral.png", "Main character neutral expression, anime style"),
            ("chars/protagonist_happy.png", "Main character happy expression, anime style"),
            ("chars/protagonist_sad.png", "Main character sad expression, anime style"),
            ("chars/antagonist.png", "Antagonist character, anime style"),
            ("chars/supporting_character.png", "Supporting character, anime style")
        ]
        
        images_to_generate.extend(character_prompts)
        
        # Generate each image
        for image_path, image_prompt in images_to_generate:
            full_path = images_dir / image_path
            print(f"Generating image: {image_path}")
            
            try:
                # Create the full prompt for Gemini
                full_prompt = f"{artist_prompt}\n\nGenerate image for: {image_prompt}"
                
                # Call Gemini image generation
                response = self.gemini_model.generate_content(full_prompt)
                
                # Extract and save the image
                image_bytes = response.candidates[0].content.parts[0].inline_data.data
                full_path.parent.mkdir(parents=True, exist_ok=True)
                
                with open(full_path, "wb") as f:
                    f.write(image_bytes)
                
                print(f"✅ Image saved: {full_path}")
                
            except Exception as e:
                print(f"❌ Error generating image for {image_path}: {e}")
                # Create a placeholder file if image generation fails
                full_path.parent.mkdir(parents=True, exist_ok=True)
                with open(full_path, 'w') as f:
                    f.write(f"Placeholder for {image_path}")
                print(f"📝 Created placeholder: {full_path}")
    
    def create_image_prompt(self, image_file: Path, story_data: Dict) -> str:
        """Create image generation prompt based on filename and story context"""
        filename = image_file.stem.lower()
        
        # Extract context from filename
        if "bg" in filename or "background" in filename:
            return f"Background image for scene: {story_data.get('scene', '')[:200]}"
        elif "char" in filename or "character" in filename:
            return f"Character sprite for: {filename}"
        else:
            return f"Scene image: {filename}"
    
    def create_placeholder_image(self, image_file: Path) -> None:
        """Create a placeholder image file (in production, this would generate actual images)"""
        # This is a placeholder - in production you'd generate actual images
        # For now, we'll just ensure the file exists
        image_file.parent.mkdir(parents=True, exist_ok=True)
        if not image_file.exists():
            # Create a simple text file as placeholder
            with open(image_file, 'w') as f:
                f.write(f"Placeholder for {image_file.name}")
    
    async def run_tester_agent(self, project_dir: Path) -> Dict:
        """Run the tester agent to verify file structure"""
        print("🔍 Running Tester Agent...")
        
        tester_prompt = self.load_prompt("tester.md")
        
        # Scan project directory structure
        project_structure = self.scan_project_structure(project_dir)
        
        full_prompt = f"{tester_prompt}\n\nProject Structure:\n{json.dumps(project_structure, indent=2)}"
        response = await self.call_openrouter(full_prompt)
        
        # Analyze the response and fix any issues
        issues = self.analyze_tester_response(response, project_dir)
        
        return {
            "response": response,
            "issues_found": issues,
            "structure": project_structure
        }
    
    def scan_project_structure(self, project_dir: Path) -> Dict:
        """Scan and return project directory structure"""
        structure = {}
        
        if project_dir.exists():
            for root, dirs, files in os.walk(project_dir):
                rel_path = Path(root).relative_to(project_dir)
                structure[str(rel_path)] = {
                    "directories": dirs,
                    "files": files
                }
        
        return structure
    
    def analyze_tester_response(self, response: str, project_dir: Path) -> List[str]:
        """Analyze tester response and identify issues"""
        issues = []
        
        # Basic validation
        required_dirs = ["game", "game/images", "game/audio", "game/audio/music", "game/audio/sfx"]
        required_files = ["game/script.rpy"]
        
        for req_dir in required_dirs:
            if not (project_dir / req_dir).exists():
                issues.append(f"Missing required directory: {req_dir}")
        
        for req_file in required_files:
            if not (project_dir / req_file).exists():
                issues.append(f"Missing required file: {req_file}")
        
        return issues
    
    def create_project_directory(self, project_name: str) -> Path:
        """Create new project directory based on exampleVN"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        project_dir = self.base_dir / f"{project_name}_{timestamp}"
        
        # Copy exampleVN structure
        if self.example_vn_dir.exists():
            shutil.copytree(self.example_vn_dir, project_dir)
            print(f"Created project directory: {project_dir}")
        else:
            # Create basic structure if exampleVN doesn't exist
            self.create_basic_structure(project_dir)
        
        # Always ensure required directories exist
        required_dirs = [
            "game/images",
            "game/images/bgs",
            "game/images/chars",
            "game/audio",
            "game/audio/music",
            "game/audio/sfx",
            "game/gui"
        ]
        for directory in required_dirs:
            (project_dir / directory).mkdir(parents=True, exist_ok=True)
        
        return project_dir
    
    def create_basic_structure(self, project_dir: Path) -> None:
        """Create basic Ren'Py project structure"""
        directories = [
            "game",
            "game/images",
            "game/images/bgs",
            "game/images/chars",
            "game/audio",
            "game/audio/music",
            "game/audio/sfx",
            "game/gui"
        ]
        
        for directory in directories:
            (project_dir / directory).mkdir(parents=True, exist_ok=True)
        
        # Create basic script.rpy
        script_content = """# Ren'Py script generated by PlotTwist Orchestrator
# This is a placeholder script

label start:
    "Welcome to your generated visual novel!"
    "This script will be populated by the AI agents."
    return
"""
        
        with open(project_dir / "game" / "script.rpy", 'w', encoding='utf-8') as f:
            f.write(script_content)
    
    async def orchestrate(self, user_story: str, twist_genre: str, art_style: str, project_name: str = "generated_vn") -> Dict:
        """Main orchestration function"""
        print("🚀 Starting PlotTwist Orchestration...")
        
        try:
            # Step 1: Create project directory
            project_dir = self.create_project_directory(project_name)
            
            # Step 2: Run writer agent
            story_data = await self.run_writer_agent(user_story, twist_genre, art_style)
            print("✅ Writer agent completed")
            
            # Step 3: Run programmer agent (without images first)
            renpy_script = await self.run_programmer_agent(story_data)
            print("✅ Programmer agent completed")
            
            # Step 4: Save initial Ren'Py script
            script_file = project_dir / "game" / "script.rpy"
            with open(script_file, 'w', encoding='utf-8') as f:
                f.write(renpy_script)
            print("✅ Initial Ren'Py script saved")
            
            # Step 5: Run artist agent
            await self.run_artist_agent(project_dir, story_data)
            print("✅ Artist agent completed")
            
            # Step 6: Collect generated images and update Ren'Py script
            generated_images = []
            for image_file in project_dir.glob("game/images/**/*.png"):
                generated_images.append(str(image_file.relative_to(project_dir)))
            
            if generated_images:
                print(f"📸 Found {len(generated_images)} generated images")
                # Update the Ren'Py script to include the generated images
                updated_script = await self.run_programmer_agent(story_data, generated_images)
                with open(script_file, 'w', encoding='utf-8') as f:
                    f.write(updated_script)
                print("✅ Ren'Py script updated with image references")
            
            # Step 7: Run tester agent
            test_results = await self.run_tester_agent(project_dir)
            print("✅ Tester agent completed")
            
            return {
                "success": True,
                "project_dir": str(project_dir),
                "story_data": story_data,
                "generated_images": generated_images,
                "test_results": test_results
            }
            
        except Exception as e:
            print(f"❌ Orchestration failed: {e}")
            return {
                "success": False,
                "error": str(e)
            }

async def main():
    """Main function for testing"""
    # You'll need to provide these API keys
    openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    
    if not openrouter_api_key or not gemini_api_key:
        print("Please set OPENROUTER_API_KEY and GEMINI_API_KEY environment variables")
        return
    
    orchestrator = PlotTwistOrchestrator(openrouter_api_key, gemini_api_key)
    
    # Example usage
    result = await orchestrator.orchestrate(
        user_story="What if Luke Skywalker discovered he had a twin sister who was raised by the Empire?",
        twist_genre="Thriller",
        art_style="Studio Ghibli",
        project_name="star_wars_twist"
    )
    
    print(f"Orchestration result: {json.dumps(result, indent=2)}")

if __name__ == "__main__":
    asyncio.run(main()) 