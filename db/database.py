from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..app import conf

engine = create_engine(conf.DATABASE_URL)
session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
