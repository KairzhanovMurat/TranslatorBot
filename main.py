import telebot
import time
from googletrans import Translator


translator=Translator()

bot=telebot.TeleBot('5361621189:AAFseIkJkfbpy34JRa1bjM_22jMkYkO_fCw')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(chat_id=message.chat.id,text= f'Пашел наху {message.from_user.first_name}. Хули пишешь сюда.')
    time.sleep(3)
    bot.send_message(chat_id=message.chat.id, text='Шчу сайпал, пиши че нить а я буду переводить на анг. Не ебу зачем Мурат меня создал, ну да ладно...')


@bot.message_handler()
def translate(message):
    translation = translator.translate(message.text)
    bot.send_message(chat_id=message.chat.id,text=translation.text)






bot.infinity_polling()