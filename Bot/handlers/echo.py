from loader import bot, logger


@bot.message_handler(content_types = ['text'])
@logger.catch
def echo(message):
  logger.debug(f"{message.session.user} Requested echo handler")
  print(message.session.user.is_admin)
  bot.send_message(message.from_user.id, f"{message.session.user} - {message.text}")
  print(message)
