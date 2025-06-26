from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class BusinessCardBase (BaseModel) : 
    
    model_config = ConfigDict(from_attributes=True)
    
    department          : Optional[str] = None
    phone_number        : Optional[str] = None
    email               : Optional[str] = None
    company_email       : Optional[str] = None
    company_number      : Optional[str] = None
    company_location    : Optional[str] = None
    sns                 : Optional[str] = None
    
class BusinessCardCreate (BusinessCardBase) : 
    name                : str = Field(..., description = "이름")
    company_name        : str = Field(..., description = "회사이름")
    
class BusinessCard (BusinessCardCreate) : 
    id                  : int
    

    
    