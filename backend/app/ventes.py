from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from .. import models, hiboutik
from ..db import SessionLocal

router = APIRouter(prefix="/ventes", tags=["Ventes"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/sync")
def sync_ventes(db: Session = Depends(get_db)):
    try:
        data = hiboutik.fetch_ventes()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    added = 0
    for s in data:
        exists = db.query(models.Vente).filter(models.Vente.id == s.get("id")).first()
        if not exists:
            db.add(models.Vente(id=s.get("id"), customer_id=s.get("customer_id"), total=s.get("total",0.0)))
            added += 1
    db.commit()
    return {"message": f"{len(data)} ventes fetched, {added} added"}

@router.get("/{customer_id}")
def get_ventes_par_client(customer_id: int, page: int = Query(1, ge=1), db: Session = Depends(get_db)):
    all_ventes = db.query(models.Vente).filter(models.Vente.customer_id == customer_id).order_by(models.Vente.id).all()
    start = (page-1)*5
    end = start+5
    return {"page": page, "total": len(all_ventes), "ventes": all_ventes[start:end]}
