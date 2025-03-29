
from ttoken import token
import random
import telebot

bot = telebot.TeleBot(token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])...
@bot.message_handler(commands=['info'])
def echo_message(message):
    bot.reply_to(message, message.text)


@bot.message_handler(content_tipes=['photo'])
def echo_message(message):
    bot.reply_to(message,'красная фотка')

@bot.message_handler(commands=['cube'])

def cube(message):
    prize=[]
    
    
    for i in range (3):

    #     bot.reply_to(message, """\
    # Выпало число \
    # """ + str(random.randint(1,6)))
        prize.append(random.randint(1,6))
    bot.reply_to(message, """\
    Выпали числа \
    """ + str(prize))

    if prize[0]==prize[1]==prize[2]:
        bot.reply_to(message, """\
    Три одинаковых! Какое везение!\
    """)

    elif prize[0]==prize[1] or prize[0]==prize[2] or prize[1]==prize[2]:
        bot.reply_to(message, """\
    Два одинаковых! Тебе везёт!\
    """)
    
bot.infinity_polling()