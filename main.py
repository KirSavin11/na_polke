import os
from telegram.ext import Application, ApplicationBuilder, CommandHandler, MessageHandler, filters, PreCheckoutQueryHandler, ContextTypes
from dotenv import load_dotenv
from bot_commands import start, get_catalog, help_command, add_to_cart, view_cart


load_dotenv()
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
PAYMENT_PROVIDER_TOKEN = os.getenv('PAYMENT_PROVIDER_TOKEN')
DATABASE_URL = os.getenv('DATABASE_URL')


if __name__ == '__main__':
    application: Application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler: CommandHandler = CommandHandler('start', start)
    application.add_handler(start_handler)

    catalog_handler: CommandHandler = CommandHandler('catalog', get_catalog)
    application.add_handler(catalog_handler)

    help_handler: CommandHandler = CommandHandler('help', help_command)
    application.add_handler(help_handler)

    add_to_cart_handler: CommandHandler = CommandHandler('add_to_cart', add_to_cart)
    application.add_handler(add_to_cart_handler)

    view_cart_handler: CommandHandler = CommandHandler('cart_items', view_cart)
    application.add_handler(view_cart_handler)

    application.run_polling()
