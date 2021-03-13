from loader import bot, logger
from telebot import types
from Bot.keyboards import  generate_select_group_markup, generate_select_course_markup


@logger.catch
@bot.message_handler(commands = ['start', 'info'])
def start_func(message):
  logger.debug(f'{message.from_user.id} {message.from_user.first_name} started the bot')
  keyboard = generate_select_course_markup()
  bot.send_message(message.chat.id, text='Оберіть курс', reply_markup=keyboard)
 