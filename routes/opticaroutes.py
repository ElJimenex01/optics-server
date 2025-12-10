from fastapi import APIRouter, Depends
from controllers import users_controller

router = APIRouter()

# Las rutas de usuarios están en /users/signup (ver users_controller.py)