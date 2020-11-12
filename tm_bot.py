import telebot

from telebot.types import Message
from config import TOKEN

bot = telebot.TeleBot(token=TOKEN)
text = 'Привет, я бот'


# @bot.message_handler(func=lambda message: True)
# def upper(message: Message):
#     bot.reply_to(message, message.text.upper())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


# @bot.message_handler(func=lambda message: True)
# def send_sticker(message: Message):
#     bot.send_sticker(message.chat.id, )


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):  # Название функции не играет никакой роли
    print(text)
    bot.send_message(message.chat.id, text)


if __name__ == '__main__':
    bot.infinity_polling()
    # bot.polling()
