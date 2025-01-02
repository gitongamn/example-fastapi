from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings
# from sqlalchemy.orm import DeclarativeBase


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
# class Base(DeclarativeBase):
#     pass

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True: #used to connect to db using SQL

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi',
#                                 user='postgres', password='123', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection successful.")
#         break
#     except Exception as error:
#         print("Database connection failed.")
#         print("Error:", error)
#         time.sleep(2)