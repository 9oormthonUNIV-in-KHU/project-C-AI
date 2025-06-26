from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database url -> need to change 
DATABASE_URL = "sqlite:///./business_cards.db" # test

engine = create_engine (
    DATABASE_URL, 
    connect_args = {"check_same_thread" : False}
)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
Base = declarative_base()