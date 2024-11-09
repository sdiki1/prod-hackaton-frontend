import telebot


token='8064671049:AAErI2A9UoX0nSrmlMH61jAW3fD5gzOxozw'
bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

  
bot.infinity_poling()