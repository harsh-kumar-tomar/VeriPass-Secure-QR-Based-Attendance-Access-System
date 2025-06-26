from fastapi import APIRouter
from fastapi.params import Depends
from database import get_db

router = APIRouter()

@router.post("/",db=Depends(get_db))
def create_session():
    pass
@router.get("/today",db=Depends(get_db))
def get_today_session():
    pass

@router.get("/{id}",db=Depends(get_db))
def get_session_detail():
    pass

@router.get("/active",db=Depends(get_db))
def get_active_sessoin():
    pass

@router.get("/{id}/participants",db=Depends(get_db))
def get_participants():
    pass
