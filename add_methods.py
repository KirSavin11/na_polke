from sqlalchemy.ext.asyncio import AsyncSession
from db_connect import connection
from asyncio import run
from models import Item
from db_connect import Category


@connection
async def create_item_example1(name: str, description: str, category: Category, price: float, session: AsyncSession) -> int:
    item = Item(name=name, description=description, category=category, price=price)
    session.add(item)
    await session.commit()
    return item.id

new_item_id = run(create_item_example1(name='Banana',
                  description='Long and yellow',
                  category='food',
                  price=0.99))
print(f'Новый товар с идентификатором {new_item_id} создан')
