import json
import os

SETTINGS_PATH = "data/guild_settings.json"
os.makedirs("data", exist_ok=True)

def load_settings():
    if not os.path.exists(SETTINGS_PATH):
        return {}
    with open(SETTINGS_PATH, "r") as f:
        return json.load(f)

def save_settings(data):
    with open(SETTINGS_PATH, "w") as f:
        json.dump(data, f, indent=2)

def set_language(guild_id, language):
    data = load_settings()
    gid = str(guild_id)
    if gid not in data:
        data[gid] = {}
    data[gid]["language"] = language
    save_settings(data)

def get_language(guild_id):
    data = load_settings()
    return data.get(str(guild_id), {}).get("language", "en")  # fallback = English
