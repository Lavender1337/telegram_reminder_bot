import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # Лучше для безопасности, но пока можем просто вставить строкой

bot = telebot.TeleBot(TOKEN or "7108696188:AAHggLRfEciprzLpbjKmMNdn5OhUbvVOuNg")

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я Напомыналыч 🤖. Напиши, что тебе напомнить.")

bot.polling(none_stop=True)
