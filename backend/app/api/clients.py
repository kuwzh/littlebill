# backend/app/api/clients.py
from fastapi import APIRouter, Query
import requests

router = APIRouter(prefix="/clients", tags=["clients"])

HIBOUTIK_API = "https://techtest.hiboutik.com/api/clients"
HIBOUTIK_AUTH = ("yanis@gmail.com", "12345")

@router.get("/search")
def search_clients(nom: str = "", email: str = ""):
    """
    Retourne une liste de clients filtrée par nom et/ou email.
    """
    try:
        response = requests.get(HIBOUTIK_API, auth=HIBOUTIK_AUTH)
        response.raise_for_status()
        clients = response.json()
    except Exception as e:
        return {"error": str(e)}

    # Filtrage simple
    if nom:
        clients = [c for c in clients if nom.lower() in c.get("nom", "").lower()]
    if email:
        clients = [c for c in clients if email.lower() in c.get("email", "").lower()]
    return clients
