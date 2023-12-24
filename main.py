import telebot
from telebot import types
import os
import csv

TOKEN = '6626418187:AAEt9Emvji2xAamYwKRKRtM5Jjre6sHpeQI'
bot = telebot.TeleBot(TOKEN,parse_mode=None)
print("Bot Started")
khadija_id = "1799125453"
girls  = ["khadija","Halima","laila"]

@bot.message_handler(commands=['start'])
def handleStart(message):
    keyboard = types.InlineKeyboardMarkup()
    btns =[]
    for girl in girls:
        btns.append(types.InlineKeyboardButton(girl,callback_data=girl))
    keyboard.add(*btns)
    bot.send_message(message.chat.id,"لائحة البنات ؟",reply_markup=keyboard)

@bot.messsage_handler(commands=['menu'])
    keyboard = types.ReplyKeyboardMarkup()
    btns = []
    for girl in girls:
        btns.append(KeyboardButton(girl))

    keyboard.add(*btns)
    bot.send_message(message.chat.id,"الفتيات اللتي تريد",reply_markup=keyboard)
    

    

@bot.callback_query_handler(func=lambda call:True)
def callVery(callback):
    if callback.data == "khadija":
        try:
            if os.path.exists("./images/"):
                with open("./images/send.png",'rb') as photo:
                    caption = "I Love you "
                    bot.send_photo(callback.message.chat.id,photo,caption=caption)
        except Exception as e:
            print(e)
    else:
        bot.send_message(callback.message.chat.id,callback.data)


@bot.message_handler(func=lambda message:True)
def handle_message(message):
    # bot.send_message(message.chat.id,"Hey Brother")
    if message.text.lower() == "khadija":
        try:
            if os.path.exists("./images/"):
                with open("./images/send.png",'rb') as photo:
                    caption = "I Love you "
                    bot.send_photo(message.chat.id,photo,caption=caption)
        except Exception as e:
            print(e)
    else:
        bot.send_message(khadija_id,message.text)



print("Bot is Pooling")
bot.infinity_polling()
