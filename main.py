import telebot
from telebot import types

bot = telebot.TeleBot('5120447001:AAFga0SiU3AGkdR0-8WeEK6NY_5bNEMzjaU')

@bot.message_handler(commands=['start'])
def start(messge):
    mess = f'privet, <b> {messge.from_user.first_name} <u>{messge.from_user.last_name}</u></b>'
    bot.send_message(messge.chat.id, mess, parse_mode='html')

# @bot.message_handler()
# def get_user_text(message):
#     if message.text == "Hello":
#        bot.send_message(message.chat.id, "Hello", parse_mode='html')
#     elif message.text == "id":
#        bot.send_message(message.chat.id, f"your ID, {message.from_user.id}", parse_mode='html')
#     elif message.text == "photo":
#         photo = open('icon.png', 'rb')
#         bot.send_photo(message.chat.id, photo)
#     else:
#         bot.send_message(message.chat.id, "I don't understand you", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Good photo!')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("go to site", url="https://google.com"))
    bot.send_message(message.chat.id, 'Good site!', reply_markup=markup)

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    website = types.KeyboardButton('website')
    start = types.KeyboardButton('Start')

    markup.add(website, start)
    bot.send_message(message.chat.id, 'Good site!', reply_markup=markup)

bot.polling(none_stop=True)