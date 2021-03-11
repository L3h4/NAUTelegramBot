import telebot
import settings
from loguru import logger

from telebot import apihelper
apihelper.ENABLE_MIDDLEWARE = True



bot = telebot.TeleBot(settings.BOT_TOKEN)





