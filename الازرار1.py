import telebot
from telebot import types

token = "5021871826:AAEDJFo13mT7kEQVUBbZg7jRvI5UwPOVF80"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def s(message):
    use = message.from_user.first_name
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text= 'DEV', callback_data= 'click1')
    button2 = types.InlineKeyboardButton(text='SOURCE CH',url= 't.me/ibnalrshed')
    keyboard.add(button1,button2)
    bot.reply_to(message, 'Hi {use}', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call:True)
def callback_data(call):
  if call.message():
      if call.data == "click1":
          bot.edit_message_text(chat_id=call.message.message_id,text='@h_69053 & @m_151la')