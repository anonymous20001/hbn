from gc import callbacks
import re
import telebot
from telebot import types
import requests
token = "5021871826:AAEDJFo13mT7kEQVUBbZg7jRvI5UwPOVF80"
bot = telebot.TeleBot(token)
@bot.message_handler(func=lambda m:True)
def total(message):
    msg = message.text
    chat = message.chat.id
    if re.match('بحث (.*?)$',msg):
        query = re.match('بحث (.*?)$',msg).group(1)
        querey = requests.get(f"https://www.youtube.com/results?searc...").content.decode('utf-8')
        urls = "\n".join(re.findall(':{"videoId":"(.*?)","', str(querey))).splitlines()
        pic = "\n".join(re.findall(':{"thumbnails":\[{"url":"(.*?)\?sqp', str(querey))).splitlines()
        names = "\n".join(re.findall('"title":{"runs":\[{"text":"(.*?)"}],"accessibility"', str(querey))).splitlines()
        name = 0
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        done = 0
        for ser in urls:
            try:
                if done == 5:
                    break
                callback = types.InlineKeyboardButton(text= f'{names[name]}', callback_data='url:{ser}')
                keyboard.add(callback)
                name +=1
                done +=1
            except:
                 pass
                 bot.reply_to(message,f'نتائج البحث: {querey}',reply_markup=keyboard)
@bot.callback_query_handler(func=lambda call:True)
def calls(call):
    try:
        data = str(calls.data)
        chat = call.chat.id
        url = data.split('url:')[1]
        bot.delete_message(chat.call.message_id)
        get_data = requests.get(f'https://api.snappea.com/v1/video/detalis?url=https://wwwyoutube.com/watch?v={url}').json()
        audio = get_data['videoInfo']['downloadInfoList'][0]['partList'][0]['urlList'][0]
        bot.send_audio(chat,audio,caption=f'Done - @{bot.get_me().username}')
    except Exception as o:
            bot.send_message(chat,o)

bot.polling()

