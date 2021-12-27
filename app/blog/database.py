from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={
                       "check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False,)

Base = declarative_base()

conn_params = psycopg2.connect(
    host="database-1.c9aweaexlowz.eu-west-2.rds.amazonaws.com",
    port=5432,
    database="AudioLifeTest",
    user="postgres",
    password="Welcome1245")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_postgresql_db():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**conn_params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')
