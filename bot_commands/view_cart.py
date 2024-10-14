"""View_cart function"""

from telegram import Update
from telegram.ext import ContextTypes
from models import CartItem
from db_connect import session


async def view_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cart_items = session.query(CartItem).filter_by(user_id=update.effective_chat.id).all()
    if cart_items:
        for item in cart_items:
            message = f'{item.item.name}: {item.quantity} шт.'
    else:
        message = 'The cart is empty now('
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message,
    )
