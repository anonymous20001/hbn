from email import message
import telebot 

token = "5021871826:AAEDJFo13mT7kEQVUBbZg7jRvI5UwPOVF80"

bot = telebot.TeleBot(token)

@bot.send_message(content_types=['كسمك'])
def s(message):
   bot.reply_to(message, 'طيزك كواد')

@bot.message_handler(content_types='طيزك')
def s(message):
    bot.reply_to(message, 'حبيبي')
