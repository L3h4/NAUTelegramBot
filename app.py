from loader import bot, logger

from Bot.middleware import middleware

from Bot.handlers import *




@logger.catch
def main():
  logger.add('logs/debug.log', format = '{time} {level} {message}', rotation = '100 KB', compression = 'zip')
  bot.polling(True)

if __name__ == "__main__":
  main()
