import telebot

TOKEN = '7699761934:AAFsXbhiUnP6jEMdJCXvntgAnwcxJHFyne4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Сәлем, досым! Мен — Muha_877_bot. Қош келдің!")

bot.polling(none_stop=True)
