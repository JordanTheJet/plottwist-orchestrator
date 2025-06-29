# PlotTwist Orchestrator 🎭

An AI-powered orchestrator that generates complete Ren'Py visual novels using multiple specialized agents. The system coordinates a writer, programmer, artist, and tester to create fully functional visual novel games.

## 🚀 Features

- **Multi-Agent Coordination**: Uses specialized AI agents for different aspects of game creation
- **OpenRouter Integration**: Leverages DeepSeek R1 0528 Qwen3 8B model for story and code generation
- **Gemini Integration**: Uses Google's Gemini for image generation and artistic tasks
- **Ren'Py Output**: Generates complete, playable Ren'Py visual novel projects
- **Automated Testing**: Includes file structure validation and quality checks

## 📋 Prerequisites

- Python 3.8 or higher
- OpenRouter API key (for DeepSeek model access)
- Google Gemini API key (for image generation)

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd plottwist-orchestrator
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys:**
   
   Option A: Environment variables
   ```bash
   export OPENROUTER_API_KEY="your_openrouter_api_key_here"
   export GEMINI_API_KEY="your_gemini_api_key_here"
   ```
   
   Option B: Enter them when prompted (see Usage section)

## 🎮 Usage

### Quick Start

Run the interactive CLI:
```bash
python run_orchestrator.py
```

The CLI will prompt you for:
1. **Story Concept**: Describe your "what if" scenario
2. **Twist Genre**: Choose from Horror, Comedy, Romance, Thriller, Mystery
3. **Art Style**: Select visual style (Studio Ghibli, anime, etc.)
4. **Project Name**: Name for your generated project

### Programmatic Usage

```python
import asyncio
from orchestrator import PlotTwistOrchestrator

async def create_game():
    orchestrator = PlotTwistOrchestrator(
        openrouter_api_key="your_key",
        gemini_api_key="your_key"
    )
    
    result = await orchestrator.orchestrate(
        user_story="What if Luke Skywalker discovered he had a twin sister raised by the Empire?",
        twist_genre="Thriller",
        art_style="Studio Ghibli",
        project_name="star_wars_twist"
    )
    
    print(f"Project created at: {result['project_dir']}")

asyncio.run(create_game())
```

## 🏗️ Architecture

The orchestrator coordinates four specialized agents:

### 1. Writer Agent 🎭
- **Model**: DeepSeek R1 0528 Qwen3 8B (via OpenRouter)
- **Purpose**: Generates complete story with characters, dialogue, and plot twists
- **Output**: Structured story data with overview, setting, characters, scenes, and plot twists

### 2. Programmer Agent 💻
- **Model**: DeepSeek R1 0528 Qwen3 8B (via OpenRouter)
- **Purpose**: Converts story into complete Ren'Py script
- **Output**: Functional Ren'Py code with branching paths and proper structure

### 3. Artist Agent 🎨
- **Model**: Google Gemini 1.5 Pro
- **Purpose**: Generates images for characters, backgrounds, and scenes
- **Output**: PNG images placed in correct project directories

### 4. Tester Agent 🔍
- **Model**: DeepSeek R1 0528 Qwen3 8B (via OpenRouter)
- **Purpose**: Validates file structure and naming conventions
- **Output**: Quality report and automatic fixes

## 📁 Project Structure

Generated projects follow the standard Ren'Py structure:

```
project_name_YYYYMMDD_HHMMSS/
├── game/
│   ├── script.rpy          # Main game script
│   ├── images/
│   │   ├── bgs/            # Background images
│   │   └── chars/          # Character sprites
│   ├── audio/
│   │   ├── music/          # Background music
│   │   └── sfx/            # Sound effects
│   └── gui/                # UI customization
└── [Ren'Py engine files]
```

## 🔧 Configuration

### API Keys

- **OpenRouter**: Get your API key from [OpenRouter](https://openrouter.ai/)
- **Gemini**: Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Model Settings

The orchestrator uses these default settings:
- **DeepSeek Model**: `deepseek/deepseek-r1-0528-qwen3-8b:free`
- **Temperature**: 0.7
- **Max Tokens**: 4000

You can modify these in the `orchestrator.py` file.

## 🎯 Example Output

The system generates complete visual novels with:

- **3 Scenes**: Beginning, choice point, and two distinct endings
- **Branching Plot**: Player choices affect story outcome
- **Character Sprites**: Multiple emotional states per character
- **Background Images**: Unique backgrounds for each scene
- **Audio Assets**: Music and sound effects
- **Professional Structure**: Ready-to-play Ren'Py project

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure your API keys are valid and have sufficient credits
2. **File Permission Errors**: Make sure you have write permissions in the project directory
3. **Network Issues**: Check your internet connection for API calls

### Debug Mode

For detailed logging, modify the orchestrator to include debug prints:
```python
# Add to orchestrator.py
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **OpenRouter** for providing access to the DeepSeek model
- **Google** for the Gemini API
- **Ren'Py** for the visual novel engine
- **The AI community** for inspiration and support

---

**Ready to create your own AI-generated visual novel? Run `python run_orchestrator.py` and let the magic begin!** ✨
