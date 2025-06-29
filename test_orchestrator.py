#!/usr/bin/env python3
"""
Test script for PlotTwist Orchestrator
"""

import os
import asyncio
import sys
from pathlib import Path

def test_imports():
    """Test if all required modules can be imported"""
    print("🔍 Testing imports...")
    
    try:
        import aiohttp
        print("✅ aiohttp imported successfully")
    except ImportError as e:
        print(f"❌ aiohttp import failed: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai imported successfully")
    except ImportError as e:
        print(f"❌ google.generativeai import failed: {e}")
        return False
    
    try:
        from orchestrator import PlotTwistOrchestrator
        print("✅ PlotTwistOrchestrator imported successfully")
    except ImportError as e:
        print(f"❌ PlotTwistOrchestrator import failed: {e}")
        return False
    
    return True

def test_file_structure():
    """Test if required files and directories exist"""
    print("\n📁 Testing file structure...")
    
    required_files = [
        "orchestrator.py",
        "run_orchestrator.py",
        "requirements.txt",
        "README.md"
    ]
    
    required_dirs = [
        "prompts",
        "exampleVN"
    ]
    
    required_prompts = [
        "prompts/writer.md",
        "prompts/programmer.md",
        "prompts/artist.md",
        "prompts/tester.md"
    ]
    
    all_good = True
    
    for file in required_files:
        if Path(file).exists():
            print(f"✅ {file} exists")
        else:
            print(f"❌ {file} missing")
            all_good = False
    
    for directory in required_dirs:
        if Path(directory).exists():
            print(f"✅ {directory}/ exists")
        else:
            print(f"❌ {directory}/ missing")
            all_good = False
    
    for prompt in required_prompts:
        if Path(prompt).exists():
            print(f"✅ {prompt} exists")
        else:
            print(f"❌ {prompt} missing")
            all_good = False
    
    return all_good

def test_api_keys():
    """Test if API keys are available"""
    print("\n🔑 Testing API keys...")
    
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")
    
    if openrouter_key:
        print("✅ OPENROUTER_API_KEY found in environment")
    else:
        print("⚠️  OPENROUTER_API_KEY not found in environment")
    
    if gemini_key:
        print("✅ GEMINI_API_KEY found in environment")
    else:
        print("⚠️  GEMINI_API_KEY not found in environment")
    
    return bool(openrouter_key and gemini_key)

async def test_basic_functionality():
    """Test basic orchestrator functionality"""
    print("\n🧪 Testing basic functionality...")
    
    openrouter_key = os.getenv("OPENROUTER_API_KEY")
    gemini_key = os.getenv("GEMINI_API_KEY")
    
    if not openrouter_key or not gemini_key:
        print("⚠️  Skipping functionality test - API keys not available")
        return True
    
    try:
        from orchestrator import PlotTwistOrchestrator
        
        orchestrator = PlotTwistOrchestrator(openrouter_key, gemini_key)
        print("✅ Orchestrator instance created successfully")
        
        # Test prompt loading
        try:
            writer_prompt = orchestrator.load_prompt("writer.md")
            if writer_prompt and len(writer_prompt) > 100:
                print("✅ Writer prompt loaded successfully")
            else:
                print("❌ Writer prompt seems too short")
                return False
        except Exception as e:
            print(f"❌ Failed to load writer prompt: {e}")
            return False
        
        # Test project directory creation
        try:
            project_dir = orchestrator.create_project_directory("test_project")
            if project_dir.exists():
                print("✅ Project directory created successfully")
                # Clean up
                import shutil
                shutil.rmtree(project_dir)
                print("✅ Test project cleaned up")
            else:
                print("❌ Project directory creation failed")
                return False
        except Exception as e:
            print(f"❌ Project directory creation failed: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Basic functionality test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 PlotTwist Orchestrator Test Suite")
    print("=" * 50)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import test failed. Please install dependencies:")
        print("pip install -r requirements.txt")
        return False
    
    # Test file structure
    if not test_file_structure():
        print("\n❌ File structure test failed. Please check repository setup.")
        return False
    
    # Test API keys
    api_keys_available = test_api_keys()
    
    # Test basic functionality
    if api_keys_available:
        functionality_ok = asyncio.run(test_basic_functionality())
        if not functionality_ok:
            print("\n❌ Basic functionality test failed.")
            return False
    else:
        print("\n⚠️  Skipping functionality test due to missing API keys.")
        print("Set OPENROUTER_API_KEY and GEMINI_API_KEY environment variables to run full tests.")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed! PlotTwist Orchestrator is ready to use.")
    print("\nTo get started:")
    print("1. Set your API keys: export OPENROUTER_API_KEY='your_key' && export GEMINI_API_KEY='your_key'")
    print("2. Run the orchestrator: python run_orchestrator.py")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 