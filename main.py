import telebot
from telebot import types
import settings
from loguru import logger

@logger.catch
def Bot():
    @bot.message_handler(commands = ['start', 'info'])
    def start_func(message):
        logger.debug(f'{message.from_user.id} {message.from_user.first_name} started the bot')
        inline_keyboard = types.InlineKeyboardMarkup()
        st_buttons = {'Курс': 'ch_curs', 'Група': 'ch_group', 'Допомога': 'hlp_pls'}
        for i , v in st_buttons.items():
            inline_keyboard.add(types.InlineKeyboardButton(text=i, callback_data=v))
        
        bot.send_message(message.chat.id, text='Оберіть функцію', reply_markup=inline_keyboard)
        
    @bot.callback_query_handler(func=lambda call:True)
    def group_processing(call):
        button = types.ReplyKeyboardMarkup(resize_keyboard=True)
        if call.data == 'ch_group':
            for i in range(1, 7 + 1):
                i = str(i)
                button.row(types.KeyboardButton(f'{i} група'))
            bot.send_message(call.from_user.id, text='Оберіть групу', reply_markup=button)
        elif call.data == 'ch_curs':
            for i in range(1, 4 + 1):
                i = str(i)
                button.row(types.KeyboardButton(f'{i} курс'))
            bot.send_message(call.from_user.id, text='Оберіть курс', reply_markup=button)
        elif call.data == 'hlp_pls':
            msg = bot.send_message(call.from_user.id, text='Your help')
        
        
if __name__ == '__main__':
    bot = telebot.TeleBot(settings.BOT_TOKEN)
    #створюється папка з логами(внесена в .gitignore)
    logger.add('logs/debug.log', format = '{time} {level} {message}', rotation = '100 KB', compression = 'zip')
    Bot()
    bot.polling(True)
    
