import json

def load_formatting_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)


def get_formatting_value(formatting, section, key, default=None):
    return formatting.get(section, {}).get(key, default)
