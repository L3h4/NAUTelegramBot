from loader import bot, logger, UM

@bot.message_handler(commands=['promote_admin'])
def promote_admin(message):
  logger.info(f"{message.session.user} Promoted to admin")
  UM.PromoteAdmin(message.session.user)
  print(message.session.user.is_admin)
