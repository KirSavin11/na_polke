"""get_catalog function"""

from telegram import Update
from telegram.ext import ContextTypes
from models import Item
from db_connect import session


async def get_catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """get_catalog function logic"""
    items = session.query(Item).all()

    if update.effective_chat is not None and items:
        message = ('Каталог товаров: \n')
        for item in items:
            message += f'{item.name} : {item.price:.2f}\n'
        message += '\nВведите название товара, чтобы добавить его в корзину'
    else:
        message = 'Пока нет товаров, приходите завтра'
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
    )
