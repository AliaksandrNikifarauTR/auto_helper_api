from fastapi import APIRouter

from api.routes import vin_info

router = APIRouter()
router.include_router(vin_info.router, tags=["test"], prefix="/vin")
