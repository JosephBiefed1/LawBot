from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import requests
import logging

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = ''

RASA_URL = 'http://localhost:5005/webhooks/rest/webhook'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hi! I am your tenant rights advisor. How can I assist you today?')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = requests.post(RASA_URL, json={"sender": str(update.message.chat_id), "message": user_message}).json()
    if response:
        update.message.reply_text(response[0]['text'])
    else:
        update.message.reply_text("Sorry, I couldn't understand that. Can you please rephrase?")

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    logger.info('Bot is running...')
    updater.idle()

if __name__ == '__main__':
    main()
