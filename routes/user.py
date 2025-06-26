from fastapi import APIRouter
from fastapi.params import Depends

from database import get_db

router = APIRouter()

@router.post("/",db = Depends(get_db))
def create_user():
    pass

@router.get("/{user_id}",db = Depends(get_db))
def get_user():
    pass

@router.get("/all",db = Depends(get_db))
def get_all_users():
    pass

@router.get("/me",db = Depends(get_db))
def get_own_profile():
    pass

@router.get("/{user_id}/qr",db = Depends(get_db))
def get_qr():
    pass
