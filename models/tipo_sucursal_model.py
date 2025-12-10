from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel

class tipoSucursal(Base):
    __tablename__ = "tipo_sucursal"

    id = Column(Integer, primary_key = True, index = True)
    tipo = Column(String(100), nullable=False)

class tipoSucursalCreate(BaseModel):
    tipo: str

class tipoSucursalUpdate(BaseModel):
    tipo: str | None = None

class TipoSucursalOut(BaseModel):
    id: int
    tipo: str

    class Config:
        from_attributes = True