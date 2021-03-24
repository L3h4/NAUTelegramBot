from loader import bot, logger


@bot.message_handler(content_types = ['document'])
@logger.catch
def file_receiving(message):
    #use admins id
    if message.from_user.id == '559592369':
        bot.send_message(message.chat.id, 'Ok, file received')
