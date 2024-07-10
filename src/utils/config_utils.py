import json

def load_formatting_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)
