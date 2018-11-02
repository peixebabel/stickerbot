# -*- coding: utf-8 -*-
#import redis
import os

token = os.environ['TELEGRAM_TOKEN']

import numpy as np
import random
import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

sticker_filepath = 'sticker.txt'

def start(bot, update):
    update.message.reply_text("Me envie um sticker e eu te enviarei outro de volta!")

def help(bot, update):
    update.message.reply_text("Me envie um sticker e eu te enviarei outro de volta!")

def random_sticker(bot, update):
	stickerfile = np.loadtxt(sticker_filepath, dtype=str)
	stickerid = update.message.sticker.file_id

	if(stickerid not in stickerfile):
		stickerfile = np.append(stickerfile, stickerid)
		np.savetxt(sticker_filepath, stickerfile, fmt='%s')	
	
	stickerid = stickerfile[random.randint(0, len(stickerfile)-1)]
	update.message.reply_sticker(stickerid)
	

def main():
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(MessageHandler(Filters.sticker, random_sticker))

    # Start the Bot
    updater.start_polling()

    # Run the bot until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT
    updater.idle()


if __name__ == '__main__':
    main()

    
