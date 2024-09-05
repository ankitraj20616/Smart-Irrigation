from database import Base
from schemas import SoilSample, Farmer
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Session

class FarmerModel(Base):
    __tablename__ = "farmer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    uname = Column(String(255))
    fname = Column(String(255))
    lname = Column(String(255))
    phone = Column(String(255))
    created_at = Column(DateTime)


class SoilSampleModel(Base):
    __tablename__ = "soil_sample"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    farmer_id = Column(Integer, ForeignKey('farmer.id'), default=None)
    address = Column(String(500))
    latitude = Column(String(255))
    longitude = Column(String(255))
    need_water = Column(Integer) # 1 means Need Water 0 means No Need
    created_at = Column(DateTime)

class SoilStore:  

    def __init__(self, db: Session): ...

    def add_farmer(self, farmer: Farmer): ...

    def get_farmer(self, uname: str): ...

    def add_sample(self, sample: SoilSample): ...

class SoilDBtore:

    def __init__(self, db: Session):
        self._db = db

    def add_farmer(self, farmer: Farmer) -> str:
        db_farmer = FarmerModel(**farmer.dict())
        self._db.add(db_farmer)
        self._db.commit()
        self._db.refresh(db_farmer)
        return Farmer.model_validate(db_farmer)
    
    def get_farmer(self, uname: str)-> str:
        db_farmer = self._db.query(FarmerModel).filter(FarmerModel.uname == uname).one_or_none()
        return db_farmer.id, db_farmer.phone

    def add_sample(self, sample: SoilSample) -> str:
        db_sample = SoilSampleModel(**sample.dict())
        self._db.add(db_sample)
        self._db.commit()
        self._db.refresh(db_sample)
        return SoilSample.model_validate(db_sample)
