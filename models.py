from sqlalchemy import Integer, String, Float, ForeignKey, text
from sqlalchemy.orm import relationship, Mapped, mapped_column, declarative_base
from db_connect import Category


Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    description: Mapped[str] = mapped_column(String, nullable=True, unique=False)
    category: Mapped[Category] = mapped_column(default=Category.goods, server_default=text("'goods'"))
    price: Mapped[float] = mapped_column(Float, nullable=True)

    def __repr__(self):
        return str(self.name)


class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]
    second_name: Mapped[str]
    delivery_address: Mapped[str]
    cart_items: Mapped[list['CartItem']] = relationship(
        'CartItem',
        back_populates='customer',
        cascade='all, delete-orphan'
    )


class CartItem(Base):
    __tablename__ = 'cart_items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    item_id: Mapped[int] = mapped_column(ForeignKey('items.id'))
    item = relationship('Item', uselist=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('customers.id'))
    customer: Mapped[int] = relationship(
        'Customer',
        back_populates='cart_items'
    )
