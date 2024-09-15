from fastapi import APIRouter, HTTPException, Depends, status
from database import SessionLocal, get_db
from sqlalchemy.orm import Session
from schemas import Farmer, FarmerLogin
from store import FarmerModel 
from starlette import status
from utils import PasswordHashing
from datetime import timedelta
from auth import JWT_Auth
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config import settings

router = APIRouter()

oauth2_schema = OAuth2PasswordBearer(tokenUrl = "token")

password_operations = PasswordHashing()
authentication = JWT_Auth()

@router.get("/", tags=["Read all data"])
def read_all(db: Session= Depends(get_db)):
    return db.query(FarmerModel).all()

# Register User
@router.post("/register/", tags= ["Registration API"])
def register(new_farmer: Farmer, db: Session = Depends(get_db)):
    farmer_in_db = db.query(FarmerModel).filter(FarmerModel.phone == new_farmer.phone).first()
    if farmer_in_db:
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= "Registration for this farmer has been done already!")
    
    
    hash_password = password_operations.hash_password(password= new_farmer.password)

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


# Login and receive jwt token
@router.post("/token")
def login(login_data: FarmerLogin,db: Session = Depends(get_db)):
    farmers = read_all(db= db)
    for farmer in farmers:
        if farmer.phone == login_data.phone and password_operations.verify_password(login_data.password, farmer.password):
            token_expire_time = timedelta(minutes= settings.ACCESS_TOKEN_EXPIRE_MINUTES)
            token = authentication.create_access_token(data= {"phone_no": farmer.phone}, expires_delta= token_expire_time)
            return token
    raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED, 
                        detail= "Incorrect Username or Password",
                        headers={"Authenticate": "Bearer"})

# Protected route - if login sucessed 
@router.get("/protected/{token}")
def protected_route(token: str):
    phone_no = authentication.verify_token(token)
    if not phone_no:
        raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,
                            detail= "Invalid token",
                            headers={"Authenticate": "Bearer"})
    return {"message": f"Hello, {phone_no}. You have accessed a protected route."}