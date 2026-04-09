import telebot
import requests
import os

TOKEN = '8638551329:AAFxDsLv0uLUBoWW8luy3RCMnzXZv0FChdI'
bot = telebot.TeleBot(TOKEN)

def get_video(url):
    api_link = f"https://www.tikwm.com/api/?url={url}"
    try:
        r = requests.get(api_link, timeout=20)
        return r.json()['data']['play']
    except:
        return None

@bot.message_handler(commands=['start'])
def start(m):
    bot.reply_to(m, "မင်္ဂလာပါ။ စောက်TikTok Link ပို့ပေးပါ။")

@bot.message_handler(func=lambda m: True)
def handle(m):
    if "tiktok.com" in m.text:
        wait = bot.reply_to(m, "လီးဘဲခဏစောင့်ပါ...")
        link = get_video(m.text)
        if link:
            bot.send_video(m.chat.id, link)
        else:
            bot.reply_to(m, "လီးကွာဗီဒီယို ရှာမတွေ့ပါ။")

bot.polling(none_stop=True)
