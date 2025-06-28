import httpx
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://valorant-api.com/v1"
HENRIK_API_KEY = os.getenv("HENRIK_API_KEY")

HEADERS = {"Authorization": HENRIK_API_KEY} if HENRIK_API_KEY else {}

def authorized_client():
    return httpx.AsyncClient(headers=HEADERS)

async def get_weapon_data():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/weapons")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_weapon_data] Fehler: {e}")
        return None

async def get_maps():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/maps")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_maps] Fehler: {e}")
        return None

async def get_agents():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/agents?isPlayableCharacter=true")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_agents] Fehler: {e}")
        return None

async def get_bundles():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/bundles")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_bundles] Fehler: {e}")
        return None

async def get_competitive_tiers():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/competitivetiers")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_competitive_tiers] Fehler: {e}")
        return None

async def get_current_season():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/seasons")
            response.raise_for_status()
            data = response.json()
            for season in data.get("data", []):
                if season.get("isActive"):
                    return season
            return None
    except Exception as e:
        print(f"[get_current_season] Fehler: {e}")
        return None

async def get_player_cards():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/playercards")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_player_cards] Fehler: {e}")
        return None

async def get_sprays():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/sprays")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_sprays] Fehler: {e}")
        return None

async def get_titles():
    try:
        async with authorized_client() as client:
            response = await client.get(f"{BASE_URL}/playertitles")
            response.raise_for_status()
            return response.json()
    except Exception as e:
        print(f"[get_titles] Fehler: {e}")
        return None
