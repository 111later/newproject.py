import requests
from bs4 import BeautifulSoup

url = 'https://1001goroskop.ru/?znak=aries'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup)
ank = soup.find_all("div", itemprop="description")
# print(ank)
clear_ank = []
for i in ank:
    clear_ank.append(i.getText())
print(clear_ank)

url1 = "https://1001goroskop.ru/?znak=pisces"
r = requests.get(url1)
soup = BeautifulSoup(r.text, "html.parser")
ank = soup.find_all("div", itemprop="description")
clear_ank1 = []
for i in ank:
    clear_ank1.append(i.getText())
print(clear_ank1)

import telebot
from telebot import types
bot = telebot.TeleBot('5150895694:AAGqRxz-FL6lB2OlDHSMhBRGW_aQfpGs5t4')

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.InlineKeyboardMarkup()
    kb_dog = types.InlineKeyboardButton(text='Овен', callback_data='aries')
    kb_cat = types.InlineKeyboardButton(text='Рыбы', callback_data='fish')
    kb.add(kb_dog, kb_cat)
    bot.send_message(message.chat.id, 'Привет, выбери знак зодиака!', reply_markup=kb)


@bot.callback_query_handler(func = lambda call: True)
def callback_inline(call):
    if call.data == 'aries':
        bot.send_message(call.message.chat.id, str(clear_ank))
    elif call.data == "fish":
        bot.send_message(call.message.chat.id, str(clear_ank1))
@bot.message_handler(commands = ['url'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn_my_site= types.InlineKeyboardButton(text='Наш сайт рыбки', url='https://1001goroskop.ru/?znak=pisces')
    markup.add(btn_my_site)
    btn_my_site = types.InlineKeyboardButton(text='Наш сайт овны', url='https://1001goroskop.ru/?znak=aries')
    markup.add(btn_my_site)
    bot.send_message(message.chat.id, "Нажми на кнопку и перейди на наш сайт.", reply_markup=markup)

bot.polling(none_stop=True)