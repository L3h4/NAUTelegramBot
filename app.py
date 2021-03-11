from loader import bot, logger

from Bot.handlers import start
from Bot.middleware import middleware




@logger.catch
def main():
  logger.add('logs/debug.log', format = '{time} {level} {message}', rotation = '100 KB', compression = 'zip')
  bot.polling(True)

if __name__ == "__main__":
  main()
