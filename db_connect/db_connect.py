from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncAttrs, async_sessionmaker
from dotenv import load_dotenv
import os
import enum


load_dotenv()
engine = create_async_engine(os.getenv('DATABASE_URL'))
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Category(str, enum.Enum):
    goods = 'goods'
    food = 'food'
    books = 'books'
    clothes = 'clothes'
    car_stuff = 'car_stuff'


def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()
                raise e
            finally:
                await session.close()
    return wrapper
