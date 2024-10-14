"""Remove item from cart function"""

from telegram import Update
from telegram.ext import ContextTypes
from models import CartItem, Item
from db_connect import session


async def remove_item(update: Update, context: ContextTypes.DEFAULT_TYPE):
    item_name = update.message.text.strip()[13:]
    item_in_cart = session.query(CartItem).join(Item, CartItem.item_id == Item.id).filter(Item.name == item_name).first()
    if item_in_cart:
        session.delete(item_in_cart)
        session.commit()
        message = f'Товар {item_name} успешно удален из корзины'
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
        )
    else:
        message = f'Товар {item_name} не найден в корзине'
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
        )
