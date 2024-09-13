from fastapi import APIRouter, HTTPException, Depends
from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas import Farmer
from store import FarmerModel
from starlette import status


router = APIRouter()

# Register User
@router.post("/register/")
def register(new_farmer: Farmer, db: Session = Depends(get_db)):
    farmer_in_db = db.query(FarmerModel).filter(FarmerModel.phone == new_farmer.phone).first()
    if farmer_in_db:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Registration for this farmer has been done already!")
    
    new_farmer_record = FarmerModel(
        id = new_farmer.id,
        uname= new_farmer.uname,
        fname= new_farmer.fname,
        lname= new_farmer.lname,
        phone= new_farmer.phone,
        password= new_farmer.password,
        created_at= new_farmer.created_at
    )
    
    db.add(new_farmer_record)
    db.commit()
    return {
        "message": "Farmer registered sucessfully!",
        "farmer": new_farmer_record
    }