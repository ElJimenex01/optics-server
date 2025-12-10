from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from database.database import get_db
from models.pacientes_model import Paciente, PacienteCreate, PacienteUpdate, PacienteOut

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])
@router.post("/create", response_model=PacienteOut)
async def create_paciente(paciente: PacienteCreate, db: AsyncSession = Depends(get_db)):

    try:
        # Verificar si el paciente ya existe SOLO dentro del mismo cliente
        query = select(Paciente).where(
            Paciente.nombres == paciente.nombres,
            Paciente.apellidos == paciente.apellidos,
            Paciente.cliente_id == paciente.cliente_id
        )
        result = await db.execute(query)
        if result.scalar_one_or_none():
            raise HTTPException(
                status_code=400,
                detail=f"Ya existe un paciente con el mismo nombre y apellidos para este cliente"
            )
        
        new_paciente = Paciente(
            nombres = paciente.nombres,
            apellidos = paciente.apellidos,
            fecha_nacimiento = paciente.fecha_nacimiento,
            cliente_id = paciente.cliente_id
        )