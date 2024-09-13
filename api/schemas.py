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
    created_at: Optional[datetime]


class SoilSample(BaseModel):
    id: Optional[str]
    farmer_id: Optional[str]
    address: Optional[str]
    latitude: Optional[str]
    longitude: Optional[str]
    need_water: Optional[int]
    created_at: Optional[datetime]

