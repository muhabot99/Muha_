
import telebot

# Токенді осы жерге қой
TOKEN = '7699761934:AAFsXbhiUnP6jEMdJCXvntgAnwcxJHFyne4'
bot = telebot.TeleBot(TOKEN)

# /start командасы
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Сәлем, досым! Мен — Muha_877_bot. Қош келдің!")

# /help командасы
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "🛠 Қол жетімді командалар:\n"
        "/start — Бастау\n"
        "/help — Көмек көрсету\n"
        "\nҚосымша мүмкіндіктерді қосу үшін хабарласыңыз!"
    )
    bot.send_message(message.chat.id, help_text)

# Ботты үзіліссіз іске қосу
bot.polling(none_stop=True)
