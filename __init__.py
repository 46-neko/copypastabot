from telegram.ext import Updater, CommandHandler
from handlers import start_handler, help_handler, randomcopypasta_handler, randomemojipasta_handler
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

updater = Updater(token ='your_token', use_context=True)
dispatcher =  updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(randomcopypasta_handler)
dispatcher.add_handler(randomemojipasta_handler)

updater.start_polling()
