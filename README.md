# File: README.md
# Termux AI Assistant

An AI-powered code assistant for Termux that utilizes Google's Vertex AI and Gemini models to generate and execute Python code.

## Installation

1. Install required dependencies in Termux:
```bash
pkg update && pkg upgrade
pkg install python python-pip git
```

2. Clone and install the package:
```bash
git clone https://github.com/AmazingZach/termux-ai-assistant.git
cd termux-ai-assistant
pip install -e .
```

3. Set up Google Cloud credentials:
- Create a Google Cloud project
- Enable Vertex AI API
- Create a service account and download credentials
- Place credentials in `~/.config/termux_ai_assistant/credentials.json`

## Usage

1. Start the assistant:
```bash
tai
```

2. Enter your code generation request in natural language.
3. Review the generated code.
4. Choose whether to execute the code.

## Features

- Natural language to code generation
- Safe code execution environment
- Rich terminal UI
- Configuration management
- Error handling and timeouts
- 
## Requirements

- Python 3.8+
- Termux
- Google Cloud account with Vertex AI access

## License

MIT License