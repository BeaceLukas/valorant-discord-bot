import json
import os

ROLE_PATH = "data/autoroles.json"
os.makedirs("data", exist_ok=True)

if not os.path.exists(ROLE_PATH):
    with open(ROLE_PATH, "w") as f:
        json.dump({}, f)

def load_roles():
    with open(ROLE_PATH, "r") as f:
        return json.load(f)

def save_roles(data):
    with open(ROLE_PATH, "w") as f:
        json.dump(data, f, indent=2)

TIERS = [
    "Unranked", "Iron", "Bronze", "Silver", "Gold",
    "Platinum", "Diamond", "Ascendant", "Immortal", "Radiant"
]
