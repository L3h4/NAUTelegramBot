import telebot
from loguru import logger
from telebot import apihelper

import settings
from Bot.UserManager import UserManager

apihelper.ENABLE_MIDDLEWARE = True


bot = telebot.TeleBot(settings.BOT_TOKEN)
UM = UserManager()




