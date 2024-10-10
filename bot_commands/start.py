"""Start bot command"""
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Function logic"""
    if update.effective_chat is not None:
        message: str = (
            'You Are Welcome'
        )

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
            reply_markup=ReplyKeyboardMarkup([['/catalog', '/cart_items', '/help']], resize_keyboard=True)
        )
