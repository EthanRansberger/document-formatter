import json
import os

def load_formatting_config(config_path):
    with open(config_path, 'r') as f:
        return json.load(f)

def merge_configs(general_config, specific_config):
    merged_config = general_config.copy()
    for key, value in specific_config.items():
        if key in merged_config and isinstance(value, dict):
            merged_config[key].update(value)
        else:
            merged_config[key] = value
    return merged_config

def get_config_path(ats_system):
    base_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_jsons', 'ats_specific')
    ats_files = {
        'taleo': 'taleo.json',
        'workday': 'workday.json',
        # Add other ATS systems and their corresponding config file names here
    }
    return os.path.join(base_path, ats_files.get(ats_system.lower(), 'general.json'))

def load_ats_config(ats_system):
    general_config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sample_jsons', 'ats_general.json')
    general_config = load_formatting_config(general_config_path)
    
    specific_config_path = get_config_path(ats_system)
    if os.path.exists(specific_config_path):
        specific_config = load_formatting_config(specific_config_path)
        return merge_configs(general_config, specific_config)
    return general_config
