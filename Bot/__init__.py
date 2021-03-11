import telebot
from telebot import types
from loguru import logger


import settings
from Bot.UserManager import UserManager, User

@logger.catch
def Bot(bot : telebot.TeleBot):
  UM = UserManager()

  @bot.message_handler(commands = ['start'])
  @UM.Wraps
  @logger.catch
  def start_func(message : types.Message, user : User):
    logger.info(f'{user} : started the bot')
    SendMesage(bot, user, f'Hello, {message.from_user.first_name}, i am NAUBOT')
  
  @bot.message_handler(content_types = ['text'])
  @UM.Wraps
  @logger.catch
  def echo(message : types.Message, user : User):
    LogRecivedText
    res = int(message.text)
    SendMesage(bot, user, message.chat.id, f'{res**2}')


def SendMesage(
    bot, 
    user, 
    text, 
    disable_web_page_preview=None, 
    reply_to_message_id=None, 
    reply_markup=None, 
    parse_mode=None, 
    disable_notification=None, 
    timeout=None
  ):
  
  logger.opt(colors=True).info(f'Send message <blue>"{text}"</blue> to <yellow>{user}</yellow>')
  
  bot.send_message(
    user.Tg_id, 
    text, 
    disable_web_page_preview=disable_web_page_preview, 
    reply_to_message_id=reply_to_message_id,
    reply_markup=reply_markup,
    parse_mode=parse_mode,
    disable_notification=disable_notification,
    timeout=timeout
  )