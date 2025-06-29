#!/usr/bin/env python3
"""
Configuration file for PlotTwist Orchestrator
"""

import os
from pathlib import Path

# API Keys (set these in environment variables or modify here)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# Model Configuration
DEEPSEEK_MODEL = "deepseek/deepseek-r1-0528-qwen3-8b:free"
GEMINI_MODEL = "gemini-1.5-pro"

# API Settings
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
TEMPERATURE = 0.7
MAX_TOKENS = 4000

# Project Settings
DEFAULT_PROJECT_NAME = "generated_vn"
BASE_DIR = Path.cwd()
PROMPTS_DIR = BASE_DIR / "prompts"
EXAMPLE_VN_DIR = BASE_DIR / "exampleVN"

# File Structure
REQUIRED_DIRECTORIES = [
    "game",
    "game/images",
    "game/images/bgs",
    "game/images/chars",
    "game/audio",
    "game/audio/music",
    "game/audio/sfx",
    "game/gui"
]

REQUIRED_FILES = [
    "game/script.rpy"
]

# Validation
def validate_config():
    """Validate configuration settings"""
    issues = []
    
    if not OPENROUTER_API_KEY:
        issues.append("OPENROUTER_API_KEY not set")
    
    if not GEMINI_API_KEY:
        issues.append("GEMINI_API_KEY not set")
    
    if not PROMPTS_DIR.exists():
        issues.append(f"Prompts directory not found: {PROMPTS_DIR}")
    
    return issues

def print_config():
    """Print current configuration"""
    print("🔧 PlotTwist Orchestrator Configuration")
    print("=" * 40)
    print(f"OpenRouter API Key: {'✅ Set' if OPENROUTER_API_KEY else '❌ Not set'}")
    print(f"Gemini API Key: {'✅ Set' if GEMINI_API_KEY else '❌ Not set'}")
    print(f"DeepSeek Model: {DEEPSEEK_MODEL}")
    print(f"Gemini Model: {GEMINI_MODEL}")
    print(f"Temperature: {TEMPERATURE}")
    print(f"Max Tokens: {MAX_TOKENS}")
    print(f"Base Directory: {BASE_DIR}")
    print(f"Prompts Directory: {PROMPTS_DIR}")
    print(f"Example VN Directory: {EXAMPLE_VN_DIR}")
    
    issues = validate_config()
    if issues:
        print("\n⚠️  Configuration Issues:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ Configuration is valid!")

if __name__ == "__main__":
    print_config() 