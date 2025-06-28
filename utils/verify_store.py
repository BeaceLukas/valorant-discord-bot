import time

# Temporärer Zwischenspeicher (kein DB-Speichern nötig)
verify_cache = {}

def store_code(user_id, code, thread):
    verify_cache[str(user_id)] = {
        "code": code,
        "created_at": time.time(),
        "thread": thread
    }

def check_code(user_id, extracted_text):
    entry = verify_cache.get(str(user_id))
    if not entry:
        return {"success": False}
    
    if entry["code"] not in extracted_text:
        return {"success": False}
    
    # Versuche Tagline im Text zu finden
    lines = extracted_text.splitlines()
    tagline = next((line.strip() for line in lines if "#" in line and len(line.strip()) <= 20), None)
    if not tagline:
        return {"success": False}
    
    return {
        "success": True,
        "tagline": tagline,
        "thread": entry["thread"]
    }
