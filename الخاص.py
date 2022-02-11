
import telebot
from telebot import types


token = "5021871826:AAEDJFo13mT7kEQVUBbZg7jRvI5UwPOVF80"
me = "1483182240"
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=['text'])
def fw(message):
    user = message,from_user.username
    bot.send_message(me, f"وصلتلك رسالة من : @{user}")
    bot.forward_message(me,message.chat.id,message.id)
    bot.reply_to(message, f"تم ارسال رسالتك بنجاح \n الرساله : {message.text}")
