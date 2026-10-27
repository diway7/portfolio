import telebot
import requests
from telebot import types

BOT_TOKEN = '8660866959:AAHDt-93CPslmUnawLUzGLAnMuM5cod3F_o'
API_KEY = '399f9abf85d66dacebb4dd69'

bot = telebot.TeleBot(BOT_TOKEN)

user_currency = {}

@bot.message_handler(commands=["start"])
def start(m):
    k = types.ReplyKeyboardMarkup(resize_keyboard=True)
    k.row("Конвертер", "Курсы") 
    k.row("Помощь")
    bot.send_message(m.chat.id, "Выбери действие:", reply_markup=k)

@bot.message_handler(func=lambda m: m.text == "Конвертер")
def converter(m):
    k = types.InlineKeyboardMarkup()
    for x in ["KZT", "USD", "EUR", "RUB"]:
        k.add(types.InlineKeyboardButton(x, callback_data=x))
    bot.send_message(m.chat.id, "Выбери валюту:", reply_markup=k)

@bot.callback_query_handler(func=lambda c: True)
def select(c):
    user_currency[c.message.chat.id] = c.data
    bot.send_message(c.message.chat.id, f"Введи сумму в {c.data}")
    bot.answer_callback_query(c.id)

@bot.message_handler(func=lambda m: m.chat.id in user_currency)
def convert(m):
    try:
        f = user_currency.pop(m.chat.id)
        amount = float(m.text.replace(",", "."))
        res = requests.get(
            f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/{f}"
        )
        data = res.json() 
    
        if data.get("result") == "success":
            result = amount * data["conversion_rates"]["KZT"]
            bot.send_message(m.chat.id, f"{amount:g} {f} = {result:.2f} KZT")
        else:
            bot.send_message(m.chat.id, "Ошибка получения курса от сервиса.")
    except ValueError:
        bot.send_message(m.chat.id, "Пожалуйста, введи числовое значение суммы.")
    except Exception as e:
        bot.send_message(m.chat.id, f"Произошла ошибка при обработке.")

@bot.message_handler(func=lambda m: m.text == "Курсы")
def rates(m):
    try:
        res = requests.get(
            f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/KZT"
        )
        data = res.json()["conversion_rates"]
        
        usd = 1 / data['USD']
        eur = 1 / data['EUR']
        rub = 1 / data['RUB']
        
        bot.send_message(
            m.chat.id,
            f"Курсы к KZT:\n"
            f"1 USD = {usd:.2f} KZT\n"
            f"1 EUR = {eur:.2f} KZT\n"
            f"1 RUB = {rub:.2f} KZT"
        )
    except Exception:
        bot.send_message(m.chat.id, "Не удалось получить курсы.")

@bot.message_handler(func=lambda m: m.text == "Помощь")
def help(m):
    bot.send_message(m.chat.id, "Выбери валюту и введи сумму.")

bot.infinity_polling()