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


@bot.message_handler(commands=['menu'])
def handleMenu(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = []
    for girl in girls:
        btns.append(types.KeyboardButton(girl))

    keyboard.add(*btns)
    bot.send_message(message.chat.id,"الفتيات اللتي تريد",reply_markup=keyboard)
    

    

@bot.callback_query_handler(func=lambda call:True)
def callVery(callback):
    chat_id = callback.message.chat.id
    if callback.data == "khadija":
        try:
            if os.path.exists("./images/"):
                with open("./images/send.png",'rb') as photo:
                    caption = "I Love you "
                    bot.send_photo(chat_id,photo,caption=caption)
        except Exception as e:
            print(e)
    else:
        parts = ["chest","tits","lips","ass","feet"]
        keyboard = types.InlineKeyboardMarkup()
        btns = []
        for part in parts:
            btns.append(types.InlineKeyboardButton(part,callback_data=part))

        keyboard.add(*btns)
        bot.delete_message(chat_id,callback.message.message_id)
        bot.send_message(chat_id,"أي طرف تريد",reply_markup=keyboard)


    

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
