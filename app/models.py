from sqlalchemy import Column, Integer, String, Text
from database import Base

class BusinessCard (Base) : 
    
    __tablename__ = "business_cards"
    
    # Auto Increment
    id                  = Column (Integer, primary_key = True, index = True)
    
    # Essential
    name                = Column (String(20), nullable = False)
    company_name        = Column (String(50), nullable = False)
    
    # Optional
    department          = Column(String(20), nullable = True)
    phone_number        = Column(String(20), nullable = True)
    email               = Column(String(20), nullable = True)
    company_email       = Column(String(20), nullable = True)
    company_number      = Column(String(20), nullable = True)
    company_location    = Column(String(20), nullable = True)
    sns                 = Column(String(100), nullable = True)
    