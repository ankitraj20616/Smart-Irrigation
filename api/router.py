from fastapi import APIRouter, HTTPException, Depends
from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas import Farmer
from store import FarmerModel
from starlette import status
from passlib.context import CryptContext 

class PasswordHashing:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes= ["bcrypt"], deprecated= "auto")
    

    def hash_password(self, password: str):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password: str, hashed_password: str):
        return self.pwd_context.verify(plain_password, hashed_password)


router = APIRouter()

# Register User
@router.post("/register/", tags= ["Registration API"])
def register(new_farmer: Farmer, db: Session = Depends(get_db)):
    farmer_in_db = db.query(FarmerModel).filter(FarmerModel.phone == new_farmer.phone).first()
    if farmer_in_db:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Registration for this farmer has been done already!")
    
    password_hasher = PasswordHashing()
    hash_password = password_hasher.hash_password(password= new_farmer.password)

    new_farmer_record = FarmerModel(
        id = new_farmer.id,
        uname= new_farmer.uname,
        fname= new_farmer.fname,
        lname= new_farmer.lname,
        phone= new_farmer.phone,
        password= hash_password,
        created_at= new_farmer.created_at
    )
    
    db.add(new_farmer_record)
    db.commit()
    return {
        "message": "Farmer registered sucessfully!",
        "farmer": new_farmer_record
    }