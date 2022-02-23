import logging

from statistics import mode
from sqlalchemy.orm import Session
from sqlalchemy import and_

from models import Device, Brand, PricesRange

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

def get_matches_multi_params(db: Session, params,  price):    
    filtered_params = {k: v for k, v in params.items() if v is not None}
    logger.warning(filtered_params)        
    query = db.query(Device)
    for attr, value in filtered_params.items():
        if attr == 'model':
            query = query.filter(getattr(Device, attr).ilike('%%%s%%' % value))
        elif attr in ['ram', 'rom']:
            query = query.filter(getattr(Device, attr) == value)
        elif attr == 'brand':
            logger.warning(value)     
            query = query.join(Brand, Device.brand_id==Brand.id).filter(Brand.brand_name == value)

    if isinstance(price, PricesRange):
        highest_price = price.highest_price
        lowest_price = price.lowest_price        
    elif price is not None:
        highest_price = int(price)*1.3
        lowest_price = int(price)*0.7
    else:
        return query.order_by(Device.price).limit(5).all()
    
    return query.filter(Device.price.between(lowest_price, highest_price)) \
        .order_by(Device.price) \
        .limit(5).all()

def get_matches_by_model(db: Session, model):
    return db.query(Device) \
            .filter(Device.model.contains(model.lower())) \
            .order_by(Device.price).limit(5)

def get_matches_by_ram(db: Session, ram):
    return db.query(Device).filter(Device.ram == ram) \
            .order_by(Device.price).limit(5)

def get_matches_by_rom(db: Session, rom):
    return db.query(Device).filter(Device.rom == rom)

def get_matches_by_price(db: Session, priceRange: PricesRange=None):
    return db.query(Device).filter(Device.price.between(priceRange.lowest_price, priceRange.higest_price))

def get_matches_by_price(db: Session, price: int=None):
    return db.query(Device).filter(Device.price.between(price*0.9, price*1.1))