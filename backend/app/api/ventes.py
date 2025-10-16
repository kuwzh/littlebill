from fastapi import APIRouter, Query, HTTPException

router = APIRouter(prefix="/ventes", tags=["Ventes"])
PAGE_LIMIT = 5

# Données factices
ventes_data = [
    {"id": 1, "client_id": 1, "produit": "Chaise", "montant": 120},
    {"id": 2, "client_id": 1, "produit": "Table", "montant": 250},
    {"id": 3, "client_id": 2, "produit": "Lampe", "montant": 45},
    {"id": 4, "client_id": 2, "produit": "Canapé", "montant": 500},
    {"id": 5, "client_id": 1, "produit": "Bureau", "montant": 180},
    {"id": 6, "client_id": 1, "produit": "Fauteuil", "montant": 75},
]

@router.get("/client/{client_id}")
def get_ventes_client(client_id: int, page: int = Query(1, ge=1)):
    """
    Récupère les ventes pour un client donné avec pagination
    """
    # Filtrer les ventes du client
    ventes_client = [v for v in ventes_data if v["client_id"] == client_id]

    if not ventes_client:
        raise HTTPException(status_code=404, detail="Aucune vente trouvée pour ce client")

    # Pagination
    start = (page - 1) * PAGE_LIMIT
    end = start + PAGE_LIMIT
    paged_ventes = ventes_client[start:end]

    return {
        "client_id": client_id,
        "page": page,
        "total_ventes": len(ventes_client),
        "ventes": paged_ventes
    }
