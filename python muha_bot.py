import telebot

bot = telebot.TeleBot("ТВОЙ_ТОКЕН")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Қош келдің! Бұл — Муxа бот.")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "Менің қолымнан келетін командалар:\n/start — Қош келдің\n/help — Көмек көрсету")

bot.polling()
