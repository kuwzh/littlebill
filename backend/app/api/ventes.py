# backend/app/api/ventes.py
from fastapi import APIRouter
import requests

router = APIRouter(prefix="/ventes", tags=["ventes"])

HIBOUTIK_API = "https://techtest.hiboutik.com/api/ventes"
HIBOUTIK_AUTH = ("yanis@gmail.com", "12345")

@router.get("/client/{client_id}")
def get_ventes(client_id: int, page: int = 1, limit: int = 5):
    """
    Retourne les ventes d'un client avec pagination simple.
    """
    try:
        response = requests.get(HIBOUTIK_API, auth=HIBOUTIK_AUTH)
        response.raise_for_status()
        ventes = response.json()
    except Exception as e:
        return {"error": str(e)}

    # Filtrer par client_id
    ventes_client = [v for v in ventes if v.get("client_id") == client_id]

    # Pagination simple
    start = (page - 1) * limit
    end = start + limit
    return {"total": len(ventes_client), "page": page, "ventes": ventes_client[start:end]}
