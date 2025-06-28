import json
import os
from datetime import datetime

DB_PATH = "users.json"

def load_db():
    if not os.path.exists(DB_PATH):
        return {}
    with open(DB_PATH, "r") as f:
        return json.load(f)

def save_db(data):
    with open(DB_PATH, "w") as f:
        json.dump(data, f, indent=2)

def link_account(discord_id, riot_tagline):
    db = load_db()
    db[str(discord_id)] = {
        "riot_tagline": riot_tagline,
        "verified_at": datetime.utcnow().isoformat()
    }
    save_db(db)

def get_linked_account(discord_id):
    db = load_db()
    return db.get(str(discord_id))
