#!/usr/bin/env python3
"""
Simple CLI interface for PlotTwist Orchestrator
"""

import os
import asyncio
from orchestrator import PlotTwistOrchestrator
import subprocess
import sys

def get_user_input():
    """Get user input for story generation"""
    print("🎭 Welcome to PlotTwist Orchestrator!")
    print("=" * 50)
    
    # Get story concept
    print("\n📖 Please describe the story you'd like to experience:")
    print("(e.g., 'What if Anakin joined the Jedi Council and never turned to the dark side?')")
    user_story = input("Story concept: ").strip()
    
    # Get twist genre
    print("\n🎬 What genre of twist would you like this story to include?")
    print("Options: Horror, Comedy, Romance, Thriller, Mystery")
    twist_genre = input("Twist genre: ").strip()
    
    # Get art style
    print("\n🎨 What visual art style should this story follow?")
    print("Options: Studio Ghibli, dark anime, Pixar-style, graphic novel, photorealistic, vintage comic")
    art_style = input("Art style: ").strip()
    
    # Get project name
    print("\n📁 What would you like to name your project?")
    project_name = input("Project name: ").strip() or "generated_vn"
    
    return user_story, twist_genre, art_style, project_name

def get_api_keys():
    """Get API keys from user or environment"""
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")
    
    if not openrouter_key:
        print("\n🔑 Please enter your OpenRouter API key:")
        openrouter_key = input("OpenRouter API Key: ").strip()
    
    if not gemini_key:
        print("\n🔑 Please enter your Gemini API key:")
        gemini_key = input("Gemini API Key: ").strip()
    
    return openrouter_key, gemini_key

async def main():
    """Main CLI function"""
    try:
        # Get API keys
        openrouter_key, gemini_key = get_api_keys()
        
        if not openrouter_key or not gemini_key:
            print("❌ API keys are required to run the orchestrator.")
            return
        
        # Get user input
        user_story, twist_genre, art_style, project_name = get_user_input()
        
        # Validate input
        if not user_story:
            print("❌ Story concept is required.")
            return
        
        if not twist_genre:
            print("❌ Twist genre is required.")
            return
        
        if not art_style:
            print("❌ Art style is required.")
            return
        
        # Create orchestrator
        print(f"\n🚀 Initializing orchestrator...")
        orchestrator = PlotTwistOrchestrator(openrouter_key, gemini_key)
        
        # Run orchestration
        print(f"\n🎬 Starting story generation...")
        print(f"Story: {user_story}")
        print(f"Genre: {twist_genre}")
        print(f"Style: {art_style}")
        print(f"Project: {project_name}")
        print("=" * 50)
        
        result = await orchestrator.orchestrate(
            user_story=user_story,
            twist_genre=twist_genre,
            art_style=art_style,
            project_name=project_name
        )
        
        # Display results
        print("\n" + "=" * 50)
        if result["success"]:
            print("✅ Orchestration completed successfully!")
            print(f"📁 Project created at: {result['project_dir']}")
            print(f"📊 Test results: {len(result['test_results']['issues_found'])} issues found")
            
            if result['test_results']['issues_found']:
                print("\n⚠️  Issues found:")
                for issue in result['test_results']['issues_found']:
                    print(f"  - {issue}")
            
            # Show instructions for playing the game
            print("\n🎮 To play your game:")
            print(f"1. Open Ren'Py and select the project at: {result['project_dir']}")
            print("2. Click 'Launch Project' in the Ren'Py launcher.")
            print("\nYou can also open the game folder or try to launch Ren'Py directly below.")
            
            # Offer to open the game folder
            print(f"\nWould you like to open the game folder now? (y/n)")
            if input().strip().lower() == 'y':
                project_dir = result['project_dir']
                if sys.platform == 'darwin':
                    subprocess.run(['open', project_dir])
                elif sys.platform == 'win32':
                    subprocess.run(['explorer', project_dir])
                else:
                    subprocess.run(['xdg-open', project_dir])
            
            # Offer to launch Ren'Py
            print(f"\nIf you have Ren'Py installed, you can try to launch your game now.")
            print(f"Would you like to try launching Ren'Py? (y/n)")
            if input().strip().lower() == 'y':
                try:
                    # This assumes renpy is on the PATH
                    subprocess.Popen(['renpy', str(result['project_dir'])])
                    print("Ren'Py launch command issued. If nothing happens, please launch manually from the Ren'Py launcher.")
                except Exception as e:
                    print(f"Could not launch Ren'Py: {e}")
        else:
            print("❌ Orchestration failed!")
            print(f"Error: {result['error']}")
        
    except KeyboardInterrupt:
        print("\n\n⏹️  Orchestration cancelled by user.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.run(main()) 