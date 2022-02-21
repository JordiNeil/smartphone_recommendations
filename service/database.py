import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

host = os.environ['host'] = '192.168.0.105'
dbname = os.environ['dbname'] = 'smartphones'
password = os.environ['password'] = '654321'
user = os.environ['user'] = 'postgres'

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}:5432/{}".format(user, password, host, dbname)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine)

Base = declarative_base()