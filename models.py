from sqlalchemy import Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, Mapped, mapped_column

Base = declarative_base()  # базовый класс для создания моделей


class Item(Base):
    __tablename__ = 'items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    price: Mapped[float] = mapped_column(Float, nullable=True)

    def __repr__(self):
        return str(self.name)


class CartItem(Base):
    __tablename__ = 'cart_items'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    item_id: Mapped[int] = mapped_column(Integer, ForeignKey('items.id'), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, default=1)
    item = relationship('Item')
