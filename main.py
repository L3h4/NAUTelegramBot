import telebot
from loguru import logger

import settings
from Bot import Bot 


def main():
    bot = telebot.TeleBot(settings.BOT_TOKEN)
    #створюється папка з логами(внесена в .gitignore)
    logger.add('logs/debug.log', format = '{time} {level} {message}', rotation = '100 KB', compression = 'zip')
    Bot(bot)
    bot.polling(True)

if __name__ == '__main__':
    main()
    
