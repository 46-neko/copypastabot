from telegram.ext import CommandHandler
from functions import start_response, help_response, randomcopypasta_response, randomemojipasta_response

start_handler = CommandHandler('start', start_response)
help_handler = CommandHandler('help', help_response)
randomcopypasta_handler = CommandHandler('randomcopypasta', randomcopypasta_response)
randomemojipasta_handler = CommandHandler('randomemojipasta', randomemojipasta_response)
