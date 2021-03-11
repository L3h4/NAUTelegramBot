from telebot import types
from loader import bot, logger

def generate_select_course_markup():
  keyboard_prefix = "sel_course"

  select_course = types.InlineKeyboardMarkup()
  for courese in range(1, 4+1, 1):
    select_course.add(types.InlineKeyboardButton(
      text=f"{courese} курс", callback_data=f"{keyboard_prefix}:{courese}"))
  return select_course


def generate_select_group_markup(course):
  keyboard_prefix = "sel_group"

  select_group = types.InlineKeyboardMarkup()
  
  for group in range(1, 7+1, 1):
    # TODO додати перевырку на підгруппу
    group = f"{group}{course}1"
    select_group.add(types.InlineKeyboardButton(
      text=group, callback_data=f"{keyboard_prefix}:{group}"))
  return select_group


#=======================

@bot.callback_query_handler(func=lambda call:"sel_course:" in call.data)
def course_processing(call):
  #print(call)
  call.data = call.data.split(":")[1]
  sel_group = generate_select_group_markup(call.data)
  bot.edit_message_text(f"Оберіть группу", call.from_user.id, call.message.id)

  bot.edit_message_reply_markup(call.from_user.id, call.message.id, reply_markup=sel_group)


@bot.callback_query_handler(func=lambda call:"sel_group:" in call.data)
def group_processing(call):
  call.data = call.data.split(":")[1]
  group = call.data
  logger.info(group)
  bot.edit_message_reply_markup(call.from_user.id, call.message.id, reply_markup=None)
  bot.edit_message_text(f"Ваша группа {group}", call.from_user.id, call.message.id)