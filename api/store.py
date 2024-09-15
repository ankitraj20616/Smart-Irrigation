from database import Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

class FarmerModel(Base):
    __tablename__ = "farmer"

    id = Column(Integer, primary_key= True, index= True, autoincrement= True)
    uname= Column(String(255), nullable = False)
    fname= Column(String(255), nullable = False)
    lname= Column(String(255), nullable = False)
    phone= Column(String(255), unique = True, nullable = False)
    password= Column(String(255), nullable= False)
    created_at= Column(String(255), default= func.now())