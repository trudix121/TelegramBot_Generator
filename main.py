import telebot
import random
import os
import time
import telebot.ext
from commands import gen

#BOTUL A FOST CREEAT 100% DE Trudix#1234  / All code has been created 100% by Trudix#1234

API_KEY = 'YOUR_TOKEN_HERE'
bot = telebot.TeleBot(API_KEY)
user_register_dict = {}


@bot.message_handler(commands=['Hello'])
def greet(message):
    bot.reply_to(message, f"{random.randint(0, 1000)}")

'''
@bot.message_handler(commands=['netflix'])
def gen_netflix(message):
    with open('C:/Users/alexa/OneDrive/Desktop/telegrambot/accounts/netflix.txt', 'r') as fg:
        account = fg.readlines()
        random_line = random.choice(account)

    bot.reply_to(message, f"Contul netflix al tau este {random_line}")


@bot.message_handler(commands=['disney'])
def gen_disney(message):
    with open('./accounts/disney+.txt', 'r') as fg:
        account = fg.readlines()
        random_account = random.choice(account)
    bot.reply_to(message, "Te rog asteapta 10 secunde")
    time.sleep(10)
    bot.reply_to(message, f'Contul tau disney+ A fost pregatit {random_account} , spor la vizionat')

'''
@bot.message_handler(commands=['help', 'start'])
def help(message):
    bot.reply_to(message, """Acestea sunt comenzile disponibile pentru botul Free-Market:
    /gen , este generator ul 
    /reportbug , poti raporta un bug  """)


@bot.message_handler(commands=['reportbug', 'bug'])
def bugreport_step1(message):
    global s
    bot.reply_to(message, 'te rog sa ne descrii bugul tau')
    # s = user_register_dict[message.chat.id]['test'] = message.text
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


'''@bot.message_handler(commands=['vpn'])
def vpn(message):
    bot.reply_to(message, "Te rog asteapta 10 secunde,")
    time.sleep(10)
    with open('./accounts/vpn.txt', 'r') as fg:
        accounts = fg.readlines()
        random_account = random.choice(accounts)
'''

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
       bot.reply_to(message, f'contul tau a fost pregatit, te rog asteapta 5 secunde pentru al revendica ')
       time.sleep(5)
       bot.reply_to(message, f"acesta este contul tau {random_lines}")
    except FileNotFoundError:
       bot.reply_to(message, 'Contul tau nu o a fost gasit in baza mea de date! Te rog sa re incerci alt cont sau sa faci un bug report ')

'''@bot.message_handler(commands=['admin'])
def admin1(message):
    bot.reply_to(message, 'parola adminului:')
    bot.register_next_step_handler(message, admin2)


def admin2(message):
    parola = user_register_dict['parola'] = message.text
    if parola == 'freemarket@!':
        bot.reply_to(message, 'ntz manilor , care i trb?')
        bot.register_next_step_handler(message, admin3)
    else:
        bot.reply_to(message, 'hoo mane ca nu e buna parola , nesimtitire ca vrei sa intrii la admini')


def admin3(message):
    bot.reply_to(message, 'scrie comanda care vrei sa o executi')
    bot.register_next_step_handler(message, admin4)

def admin4(message):
    admin4 = user_register_dict['comenzi admin'] = message.text
    admin5 = user_register_dict['comenzi admin5'] = message.text
    if admin4 == 'coduri':
        print('a  inceput generarea de coduri pe luna martie!')
        bot.reply_to(message, 'generarea a inceput')
        with open('./coduri/coduri_martie.txt', 'w') as fg:
            while True:
                fg.write(str(random.randint(0, 100000)))
                if admin5 == 'stop':
                 break
                bot.reply_to(message, 'generarea a fost oprita')'''






@bot.message_handler(commands=['stock'])
def stock(message):
 path = './accounts/'
 bot.reply_to(message, 'te rog asteapta 5 secunde')
 time.sleep(5)
 import os
 fileList = os.listdir(path)
 for file in fileList:
    bot.reply_to(message, f'{file}, Conturi:{len(file)}')





















print("Botul a fost pornit!")
bot.polling()
