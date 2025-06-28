import json
import os
from datetime import datetime

CACHE_PATH = "data/mmr_cache.json"
os.makedirs("data", exist_ok=True)

if not os.path.exists(CACHE_PATH):
    with open(CACHE_PATH, "w") as f:
        json.dump({}, f)

def load_cache():
    with open(CACHE_PATH, "r") as f:
        return json.load(f)

def save_cache(data):
    with open(CACHE_PATH, "w") as f:
        json.dump(data, f, indent=2)

def update_cache(user_id: int, data: dict):
    cache = load_cache()
    cache[str(user_id)] = {
        **data,
        "updated_at": datetime.utcnow().isoformat()
    }
    save_cache(cache)

def get_cached_account(user_id: int):
    cache = load_cache()
    return cache.get(str(user_id))
