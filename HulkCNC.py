import telebot
from telebot import types

bot = telebot.TeleBot('5120447001:AAFga0SiU3AGkdR0-8WeEK6NY_5bNEMzjaU')

@bot.message_handler(commands=['start'])
def start(messge):
    mess = f'privet, <b> {messge.from_user.first_name} <u>{messge.from_user.last_name}</u></b>'
    bot.send_message(messge.chat.id, mess, parse_mode='html')