import os
import telebot
import random
import time
import telebot.ext
from commands import gen

API_KEY = 'YOUR_TOKEN_HERE'
bot = telebot.TeleBot(API_KEY)
user_register_dict = {}


@bot.message_handler(commands=['Hello'])
def greet(message):
    bot.reply_to(message, f"{random.randint(0, 1000)}")


@bot.message_handler(commands=['help', 'start'])
def help(message):
    bot.reply_to(message, )


@bot.message_handler(commands=['reportbug', 'bug'])
def bugreport_step1(message):
    global s
    bot.reply_to(message, 'te rog sa ne descrii bugul tau')

    bot.register_next_step_handler(message, bugreport_step2)


def bugreport_step2(message):
    test = user_register_dict['bug'] = message.text
    with open(f"./bug_reports/bug_report_ID_{random.randint(0, 10000)}.txt", 'x') as rb:
        rb.write(f'Aveti un report , mesajul este: {test}')
    bot.reply_to(message, 'Bug ul a fost raportat ')
    print('Bug: ' + test)


@bot.message_handler(commands=['ping'])
def ping(message):
    bot.reply_to(message, "Pong")


@bot.message_handler(commands=['gen'])
def gen1(message):
    bot.reply_to(message, 'te rog asteapta 5 secunde')
    time.sleep(5)
    bot.reply_to(message, 'te rog sa specifici ce cont vrei')
    bot.register_next_step_handler(message, gen2)



def gen2(message):
    x = user_register_dict['cont'] = message.text
    try:
        with open(f'./accounts/{x}.txt', 'r') as fg:
            account = fg.readlines()
            random_lines = random.choice(account)
            bot.reply_to(message, f'contul tau a fost pregatit ({random_lines})')
    except FileNotFoundError:
        bot.reply_to(message,
                     'Contul tau nu o a fost gasit in baza mea de date! Te rog sa re incerci alt cont sau sa faci un bug report ')


'''@bot.message_handler(commands=['admin'])
def admin1(message):
    bot.reply_to(message, 'parola adminului:')
    bot.register_next_step_handler(message, admin2)


def admin2(message):
    parola = user_register_dict['parola'] = message.text
    if parola == 'freemarket@!':
        bot.register_next_step_handler(message, admin3)
    else:
        bot.reply_to(message, 'hoo mane ca nu e buna parola , nesimtitire ca vrei sa intrii la admini')


def admin3(message):
    bot.reply_to(message, 'scrie comanda care vrei sa o executi')
    bot.register_next_step_handler(message, admin4)


def admin4(message):
    '''


@bot.message_handler(commands=['stock'])
def stock(message):
 import os
 files = os.listdir('./accounts')




bot.polling()
