import logging
import uvicorn 

from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

import crud, models, schemas
from DevicesParser import DevicesParser
from database import SessionLocal, engine
from utils import constants

models.Base.metadata.create_all(bind=engine)

logger = logging.getLogger()
logger.setLevel(logging.WARNING)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/get_recommendations/", response_model=List[schemas.Device])
def get_recommendations(
        model: str=None, 
        ram: str=None, 
        rom: str=None, 
        price: str=None, 
        brand: constants.BRAND_ENUM=constants.BRAND_ENUM.default, 
        db: Session = Depends(get_db)):

    if ((model is None or model.strip() == '') 
        and ram is None 
        and rom is None 
        and (brand == constants.BRAND_ENUM.default)
        and price is None):
        raise HTTPException(
            status_code=400,
            detail='You must send any device information.'
        )
    else:
        params = {}

        device = DevicesParser(model, ram, rom, brand)
        params['ram'] = device.ram
        params['rom'] = device.rom
        params['brand'] = device.brand
        params['model'] = device.model     
        matches = crud.get_matches_multi_params(db, params, price)
        while(matches is None and len(params)>2):
            params.popitem()
            logger.warning(params)
            new_matches = crud.get_matches_multi_params(db, params, price=None)
            matches = matches.append(new_matches)

        return matches

##Comment these two lines when running with docker
# if __name__ == '__main__':
#     uvicorn.run(app, host='0.0.0.0', port=8080)