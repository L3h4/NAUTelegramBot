import telebot
from loader import bot, logger, UM

@bot.middleware_handler(update_types=['message'])
@UM.MidlewareWrapper
def middleware(bot_instance, message):
  logger.opt(colors=True).info(f'<yellow>{message.session.user}</yellow> : <blue>"{message.text}"</blue>')

  

