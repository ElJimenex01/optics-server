from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship
from database.database import Base
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Sucursal(Base):

    __tablename__ = "sucursales"

    id = Column(Integer, primary_key = True, index = True)
    sucursal = Column(String(100), nullable=False)
    tipo_sucursal_id = Column(Integer, nullable=False)
    dependencia = Column(String(100), nullable=False)
    mondeda = Column(String(10), nullable=False)
    razon_social = Column(String(200), nullable=False)
    estado_sucursal_id = Column(Integer, nullable=False)

class SucursalCreate(BaseModel):
    sucursal: str
    tipo_sucursal_id: int
    dependencia: str
    mondeda: str
    razon_social: str
    estado_sucursal_id: int

class SucursalUpdate(BaseModel):
    sucursal: str | None = None
    tipo_sucursal_id: int | None = None
    dependencia: str | None = None
    mondeda: str | None = None
    razon_social: str | None = None
    estado_sucursal_id: int | None = None

class SucursalOut(BaseModel):
    id: int
    sucursal: str
    tipo_sucursal_id: int
    dependencia: str
    mondeda: str
    razon_social: str
    estado_sucursal_id: int

    class Config:
        from_attributes = True
