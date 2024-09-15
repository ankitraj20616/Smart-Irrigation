from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Farmer(BaseModel):
    id: Optional[str]
    uname: Optional[str]
    fname: Optional[str]
    lname: Optional[str]
    phone: Optional[str]
    password: Optional[str]
    created_at: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "id": "ID of user",
                "uname": "User Name",
                "fname": "First Name",
                "lname": "Last Name",
                "phone": "Phone",
                "password": "Password",
                "created_at": "Date Time(DD-MM-YY//Time:Min) of creation"
            }
        }


class FarmerLogin(BaseModel):
    phone: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "phone": "Registered Phone Number",
                "password": "Your Password"
            }
        }



class SoilSample(BaseModel):
    id: Optional[str]
    farmer_id: Optional[str]
    address: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    need_water: Optional[int]
    created_at: Optional[datetime]

