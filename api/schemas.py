from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class SoilSample(BaseModel):
    farmer_id: Optional[str]
    address: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    need_water: Optional[int]
    created_at: Optional[datetime]

class SoilSampleResponse(SoilSample):
    id: str

    class Config:
        from_attributes = True

class Farmer(BaseModel):
    uname: Optional[str]
    fname: Optional[str]
    lname: Optional[str]
    phone: Optional[str]
    created_at: Optional[datetime]

class FarmerResponse(Farmer):
    id: str
    
    class Config:
        from_attributes = True