from telegram.ext import Updater
from bot_config import *
import telebot
from telebot import types

bot = telebot.TeleBot(TOKEN)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_address = types.KeyboardButton('Store Addresses', request_location=True)
btn_payment = types.KeyboardButton('Payment Methods')
btn_delivery = types.KeyboardButton('Delivery Methods')
markup_menu.add(btn_address, btn_delivery, btn_payment)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hi I'm bot", reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Payment Methods':
        bot.reply_to(message, 'Cash', reply_markup=markup_menu)
    elif message.text == 'Delivery Methods':
        bot.reply_to(message, 'Courier delivery', reply_markup=markup_menu)
    else:
        bot.reply_to(message, message.text, reply_markup=markup_menu)


bot.message_handler(func=lambda message: True, content_types=['location'])
def store_location(message):
    lon = message.location.logitude
    lat = message.location.latitude

    distance = []


bot.polling()


