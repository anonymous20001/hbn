import requests
import telebot

token = "5021871826:AAEDJFo13mT7kEQVUBbZg7jRvI5UwPOVF80"
#@h_690531
bot = telebot.TeleBot(token)

@bot.message_handler(func=lambda m:True)
def v(message):
    msg = message.text
    bot.send_message(message.chat.id, "انتظر لحظة")
    if "https://vm.tiktok" not in msg: 
        exit()
    elif "https://vm.tiktok" in msg:
          url = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={msg}&key=godownloader.com").json() 
          nomark = url['video_no_watermark']
          photo = url['author_cover']
          bot.send_video(message.chat.id,nomark,caption=f"<strong>تم @ibnalrshedbot(:</strong>",parse_mode="html")
   
bot.polling()