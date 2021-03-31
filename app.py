from loader import bot, logger

from Bot.middleware import middleware

from Bot.handlers import *

from Bot.handlers import PDF_receiving


@logger.catch
def main():
  logger.add('logs/debug.log', format = '{time} {level} {message}', rotation = '100 KB', compression = 'zip')
  echo
  PDF_receiving.file_receiving
  bot.polling(True)

if __name__ == "__main__":
  main()
