from datetime import date as date_type
from email import message
from multiprocessing import Value
from typing import List, Optional

from pydantic import BaseModel

class Vendor(BaseModel):
    name: str
    web_page: Optional[str] = None
    
    class Config:
        orm_mode = True

class Brand(BaseModel):
    brand_name: str

    class Config:
        orm_mode = True

class Device(BaseModel):
    model: str
    vendor: Vendor
    ram: Optional[int] = None
    rom: Optional[int] = None
    brand: Optional[Brand] = None    
    last_seen: Optional[date_type] = None  
    price: str

    class Config:
        orm_mode = True

class Recommendations(BaseModel):
    devices: List[Device] = []
    message: Optional[str] = ''
