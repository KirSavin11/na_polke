"""help_command logic"""
from telegram import Update
from telegram.ext import ContextTypes


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Function logic"""
    if update.effective_chat is not None:
        message = (
            'Here is nobody except you'
        )
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message,
        )
