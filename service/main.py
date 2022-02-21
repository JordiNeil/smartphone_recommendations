import logging
import uvicorn 
from pyexpat import model
import string

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud, models, schemas
from DevicesParser import DevicesParser
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/get_recommendations/", response_model=List[schemas.Device])
def get_recommendations(value, ram: str=None, rom: str=None, price: str=None, db: Session = Depends(get_db)):

    if value is None or value.strip() == '':
        raise HTTPException(
            status_code=400,
            detail='You must send any device information.'
        )
    else:
        params = {}

        device = DevicesParser(value, ram, rom)
        params['ram'] = device.ram
        params['rom'] = device.rom
        params['model'] = device.model        
        matches = crud.get_matches_multi_params(db, params, price)
        while(matches is None and len(params)>2):
            params.popitem()
            logger.warning(params)
            new_matches = crud.get_matches_multi_params(db, params, price=None)
            matches = matches.append(new_matches)

        return matches

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8080)