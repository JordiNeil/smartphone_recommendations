from enum import Enum
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from database import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True)
    model = Column(String)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    vendor_id = Column(Integer, ForeignKey('vendors.id'))
    ram = Column(Integer)
    rom = Column(Integer)
    last_seen = Column(Date)
    price = Column(String)
    network = Column(String)

    brand = relationship("Brand", back_populates="devices")
    vendor = relationship("Vendor", back_populates="devices")

class Brand(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True)
    brand_name = Column(String)

    devices = relationship("Device", back_populates="brand")

class Vendor(Base):
    __tablename__ = "vendors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    web_page = Column(String)

    devices = relationship("Device", back_populates="vendor")

class PricesRange():

    highest_price: int = 0
    lowest_price: int = 0
