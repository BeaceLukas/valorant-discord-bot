import time

# Temporärer Zwischenspeicher
verify_cache = {}

# Speichert einen Verifizierungscode mit Zeitstempel und Thread (optional)
def store_code(user_id, code, thread):
    verify_cache[str(user_id)] = {
        "code": code,
        "created_at": time.time(),
        "thread": thread
    }

# Prüft, ob ein gültiger Code vorhanden und im Screenshot enthalten ist
def check_code(user_id, extracted_text):
    entry = verify_cache.get(str(user_id))
    if not entry:
        return {"success": False}

    # Ablaufprüfung: 10 Minuten
    if time.time() - entry["created_at"] > 600:
        return {"success": False}

    if entry["code"] not in extracted_text:
        return {"success": False}

    # Tagline extrahieren
    lines = extracted_text.splitlines()
    tagline = next((line.strip() for line in lines if "#" in line and len(line.strip()) <= 20), None)
    if not tagline:
        return {"success": False}

    return {
        "success": True,
        "tagline": tagline,
        "thread": entry["thread"]
    }
