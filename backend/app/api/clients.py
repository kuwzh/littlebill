from fastapi import APIRouter, Query

router = APIRouter(prefix="/clients", tags=["clients"])


clients_data = [
    {"id": 1, "nom": "Dupont", "email": "dupont@mail.com"},
    {"id": 2, "nom": "Martin", "email": "martin@mail.com"},
    {"id": 3, "nom": "Durand", "email": "durand@mail.com"},
]

@router.get("/search")
def search_clients(nom: str = Query(None), email: str = Query(None)):

    results = clients_data

    if nom:
        results = [c for c in results if nom.lower() in c["nom"].lower()]

    if email:
        results = [c for c in results if email.lower() in c["email"].lower()]

    return results
