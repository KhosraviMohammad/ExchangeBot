import telebot

bot = telebot.TeleBot(r"6217934433:AAF-CrHootfw4BvAFHKBpSN7cIeZA0oIPlM")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()