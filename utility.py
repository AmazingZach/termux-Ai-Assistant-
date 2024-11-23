
# File: termux_ai_assistant/utils.py
import os
import yaml
from pathlib import Path

def load_config():
    """Load configuration from YAML file."""
    config_path = Path.home() / ".config" / "termux_ai_assistant" / "config.yaml"
    
    # Create default config if it doesn't exist
    if not config_path.exists():
        os.makedirs(config_path.parent, exist_ok=True)
        default_config = {
            "credentials_path": str(Path.home() / ".config" / "termux_ai_assistant" / "credentials.json"),
        }
        
        with open(config_path, 'w') as f:
            yaml.dump(default_config, f)
    
    # Load config
    with open(config_path) as f:
        return yaml.safe_load(f)