import telebot
from telebot import types
import settings



bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(content_types=["text"])
def on_text(message : types.Message):
  bot.reply_to(message, message.text)




bot.polling(True)