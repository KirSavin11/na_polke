"""Add item to cart function"""

from telegram import Update
from telegram.ext import ContextTypes
from models import CartItem, Item
from db_connect import session


async def add_to_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item_names = context.args

    for item_name in item_names:
        item = session.query(Item).filter_by(name=item_name).first()
        if item:
            item_in_cart = session.query(CartItem).filter_by(user_id=update.effective_user.id, item_id=item.id).first()
            if item_in_cart:
                item_in_cart.quantity += 1
            else:
                item_in_cart = CartItem(user_id=update.effective_chat.id, item_id=item.id)
                session.add(item_in_cart)
            session.commit()
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f'Товар {item.name} добавлен в корзину',
            )
        else:
            message = ''
            for item in item_names:
                message += f'Товар {item} не найден\n'
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=message,
            )
