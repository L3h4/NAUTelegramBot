from loader import bot, logger
from telebot import types

@logger.catch
@bot.message_handler(commands=["start"])
def on_text(message : types.Message):
  bot.reply_to(message, message.text)
  logger.debug(message.session)
