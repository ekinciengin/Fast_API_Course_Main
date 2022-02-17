from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Welcome1245@database-1.c9aweaexlowz.eu-west-2.rds.amazonaws.com:5432/postgres"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
