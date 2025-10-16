from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from .. import models, hiboutik
from ..db import SessionLocal

router = APIRouter(prefix="/clients", tags=["Clients"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sync")
def sync_clients(db: Session = Depends(get_db)):
    try:
        data = hiboutik.fetch_clients()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    added = 0
    for c in data:
        exists = db.query(models.Client).filter(models.Client.id == c.get("id")).first()
        if not exists:
            db.add(models.Client(id=c.get("id"), name=c.get("name"), email=c.get("email","")))
            added += 1
    db.commit()
    return {"message": f"{len(data)} clients fetched, {added} added"}

@router.get("/")
def get_clients(name: str = Query(None), email: str = Query(None), db: Session = Depends(get_db)):
    q = db.query(models.Client)
    if name:
        q = q.filter(models.Client.name.contains(name))
    if email:
        q = q.filter(models.Client.email.contains(email))
    return q.all()
