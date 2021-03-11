import telebot
from loader import bot, logger

@bot.middleware_handler(update_types=['message'])
def middleware(bot_instance, message):
  logger.info(f"{message.chat.id} : {message.text}")
  message.session = "session"

