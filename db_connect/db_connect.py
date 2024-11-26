from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import enum


load_dotenv()
engine = create_engine(os.getenv('DATABASE_URL'))
Session = sessionmaker(bind=engine)
session = Session()


class Category(str, enum.Enum):
    goods = 'goods'
    food = 'food'
    books = 'books'
    clothes = 'clothes'
    car_stuff = 'car_stuff'
