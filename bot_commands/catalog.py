"""get_catalog function"""
from telegram import Update
from telegram.ext import ContextTypes


async def get_catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """get_catalog function logic"""
    if update.effective_chat is not None:
        message = (
            ''
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
        )
