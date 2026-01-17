import telebot
from bot_logic import gen_pass, gen_emodji, flip_coin, # Импортируем функции из bot_logic
import requests

TOKEN = '8591728276:AAF7pYM9aDwGfaNPkK8zTQGDAtwLTI8FJe4'
bot = telebot.TeleBot("TOKEN")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}! Я твой Telegram бот. Напиши команду /hello, /bye, /pass,/mem, /emodji или /coin  ") #добавил имя как обращение

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, f"Привет {message.from_user.first_name}! Как дела?") #добавил имя как обращение

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, f"Пока {message.from_user.first_name}! Удачи!") #добавил имя как обращение
 # усовершенствовал пароль, теперь можно выбрать длинну пароля
@bot.message_handler(commands=['pass'])

def send_password(message):
    bot.reply_to(message, "из скольки символов?")
    @bot.message_handler(func=lambda message: message.text.isdigit())   
    def send_passwordlen(message):
            password = gen_pass(int(message.text))  
            bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji']) #генерирует смайлики
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin']) #подбрасывает монетку
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin} ")

# Запускаем бота

bot.polling()
