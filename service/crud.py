import logging

from statistics import mode
from sqlalchemy.orm import Session
from sqlalchemy import and_

import models, schemas

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

def get_matches_multi_params(db: Session, params,  price):    
    filtered_params = {k: v for k, v in params.items() if v is not None}
    logger.warning(filtered_params)        
    query = db.query(models.Device)
    for attr, value in filtered_params.items():
        if attr == 'model':
            query = query.filter(getattr(models.Device, attr).ilike('%%%s%%' % value))
        elif attr in ['ram', 'rom']:
            query = query.filter(getattr(models.Device, attr) == value)
    if isinstance(price, models.PricesRange):
        highest_price = price.highest_price
        lowest_price = price.lowest_price        
    elif price is not None:
        highest_price = price*1.1
        lowest_price = price*0.9
    else:
        return query.order_by(models.Device.price).limit(5).all()
    
    return query.filter(models.Device.price.between(lowest_price, highest_price)) \
        .order_by(models.Device.price) \
        .limit(5).all()

def get_matches_by_model(db: Session, model):
    return db.query(models.Device) \
            .filter(models.Device.model.contains(model.lower())) \
            .order_by(models.Device.price).limit(5)

def get_matches_by_ram(db: Session, ram):
    return db.query(models.Device).filter(models.Device.ram == ram) \
            .order_by(models.Device.price).limit(5)

def get_matches_by_rom(db: Session, rom):
    return db.query(models.Device).filter(models.Device.rom == rom)

def get_matches_by_price(db: Session, priceRange: models.PricesRange=None):
    return db.query(models.Device).filter(models.Device.price.between(priceRange.lowest_price, priceRange.higest_price))

def get_matches_by_price(db: Session, price: int=None):
    return db.query(models.Device).filter(models.Device.price.between(price*0.9, price*1.1))