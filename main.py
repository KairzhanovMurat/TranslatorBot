import telebot
import time
from googletrans import Translator
import os


translator=Translator()

bot=telebot.TeleBot(os.getenv('token'))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id,text= f'Здарова {message.from_user.first_name}.')
    time.sleep(3)
    bot.send_message(chat_id=message.chat.id, text=' пиши че нить а я буду переводить на анг. ')


@bot.message_handler()
def translate(message):
    translation = translator.translate(message.text)
    bot.send_message(chat_id=message.chat.id,text=translation.text )






bot.infinity_polling()