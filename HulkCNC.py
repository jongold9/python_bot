import telebot
from telebot import types

bot = telebot.TeleBot('5120447001:AAFga0SiU3AGkdR0-8WeEK6NY_5bNEMzjaU')

@bot.message_handler(commands=['start'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    start = types.KeyboardButton('/start')
    help = types.KeyboardButton('help')
    website = types.KeyboardButton('website')

    markup.add(start, help, website)

    bot.send_message(message.chat.id, 'Привет, в меню снизу ты можешь выбрать интересующую тебя тему', reply_markup=markup)

@bot.message_handler()
def get_user_text(message):
    if message.text == "help":
        bot.send_message(message.chat.id, "Hello, I help you", parse_mode='html')
    elif message.text == "website":
        bot.send_message(message.chat.id, "https://google.com", parse_mode='html')
    else:
        bot.send_message(message.chat.id, "I don't understand you", parse_mode='html')


bot.polling(none_stop=True)