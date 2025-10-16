# backend/main.py
from fastapi import FastAPI
from app.api import clients, ventes

app = FastAPI(title="LittleBill API")

app.include_router(clients.router)
app.include_router(ventes.router)

@app.get("/")
def root():
    return {"message": "Bienvenue sur l'API LittleBill"}
