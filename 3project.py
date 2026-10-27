import telebot  
import threading
import time

bot = telebot.TeleBot("8892050581:AAHRcoAChYuf9WZuS_OGJ5Fc6HPp4Pt6RJo")

water = {}
reminders = {}


# /start
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я помогу следить за водой.\n\n"
        "Команды:\n"
        "/setreminder 1 — напоминать каждый час\n"
        "/setreminder 2 — каждые 2 часа\n"
        "/drank 300 — выпил 300 мл\n"
        "/status — проверить баланс воды"
    )


# Установка напоминания
@bot.message_handler(commands=["setreminder"])
def set_reminder(message):
    try:
        hours = int(message.text.split()[1])

        if hours <= 0:
            raise ValueError

        reminders[message.chat.id] = hours * 3600

        bot.send_message(
            message.chat.id,
            f"&#9200; Напоминание установлено!\n"
            f"Буду напоминать каждые {hours} ч."
        )

    except:
        bot.send_message(
            message.chat.id,
            "&#10060; Напиши так: /setreminder 1"
        )


# Добавление выпитой воды
@bot.message_handler(commands=["drank"])
def drank(message):
    try:
        amount = int(message.text.split()[1])

        if amount <= 0:
            raise ValueError

        user = message.chat.id
        water[user] = water.get(user, 0) + amount

        bot.send_message(
            user,
            f"&#128167; Записано: {amount} мл\n"
            f"Всего сегодня: {water[user]} мл"
        )

    except:
        bot.send_message(
            message.chat.id,
            "&#10060; Напиши так: /drank 300"
        )


# Статус
@bot.message_handler(commands=["status"])
def status(message):
    user = message.chat.id
    drunk = water.get(user, 0)
    left = max(2000 - drunk, 0) 

    bot.send_message(
        user,
        f" Выпито сегодня: {drunk} мл\n"
        f" Осталось: {left} мл"
    )


# Поток напоминаний
def reminder():
    while True:
        time.sleep(60)

        for user, seconds in list(reminders.items()):
            if not hasattr(reminder, "time"):
                reminder.time = {}

            reminder.time[user] = reminder.time.get(user, 0) + 60

            if reminder.time[user] >= seconds:
                bot.send_message(
                    user,
                    "&#128167; Не забывай пить воду!\n"
                    "Выпей стакан воды &#11088;"
                )
                reminder.time[user] = 0


threading.Thread(
    target=reminder,
    daemon=True
).start()


print("&#128167; Бот запущен!")
bot.infinity_polling()