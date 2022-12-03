from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

from os import environ

engine = create_engine(environ.get('DATABASE_URL'), echo = True)
session = scoped_session(sessionmaker(bind=engine))
meta = MetaData(engine)
Base = declarative_base(metadata=meta)
