from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    ventes = relationship("Vente", back_populates="client")

class Vente(Base):
    __tablename__ = "ventes"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("clients.id"))
    total = Column(Float)
    client = relationship("Client", back_populates="ventes")
