from store import SoilStore, SoilDBtore
from service import SoilService
from schemas import Farmer, SoilSample, FarmerResponse
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, Query
from database import get_db

def get_soil_store(db: Session = Depends(get_db)) -> SoilStore:
    return SoilDBtore(db=db)


def get_soil_service(store: Session = Depends(get_soil_store)):
    return SoilService(store=store)

router = APIRouter()


@router.post("/add_farmer")
def add_farmer(
    farmer_request: Farmer,
    soil_service: SoilService = Depends(get_soil_service),
) -> FarmerResponse:
    return soil_service.add_farmer(request=farmer_request)

@router.post("/test_soil")
def test_soil(
    farmer_uname: str = Query(...),
    area_name: str = Query(...),
    city_name: str = Query(...),
    soil_service: SoilService = Depends(get_soil_service),
) -> str:
    return soil_service.add_sample(
        farmer_uname=farmer_uname,
        area_name=area_name,
        city_name=city_name
    )