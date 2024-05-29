import telebot
import requests
import json

bot = telebot.TeleBot('7067318674:AAEz0pKA6NLkN73EXc0ruAvQLSMNBL1oFyY')
API = '403a4f0d92c19ada104d758d383b33c9'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! Напиши название города')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Погода в грооде сейчас: {temp}')

        image = 'fun.png' if temp > 10.0 else 'nofun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Такого города нет')

bot.polling(none_stop=True)














