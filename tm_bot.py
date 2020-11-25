import telebot

# from telebot.types import Message
from config import TOKEN
from dialogflou import DialogFlow
from semantic import get_related_words

bot = telebot.TeleBot(token=TOKEN)
text = 'Привет, я бот'
dialog = DialogFlow()


# @bot.message_handler(func=lambda message: True)
# def upper(message: Message):
#     bot.reply_to(message, message.text.upper())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, что ты от меня хочешь?")


# @bot.message_handler(func=lambda message: True)
# def send_sticker(message: Message):
#     bot.send_sticker(message.chat.id, )

# @bot.message_handler(content_types=['text'])
# def repeat_all_messages(message):
#     message_text = message.text
#     answer = dialog.get_answer(message_text)
#     bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def send_related_words(message):
    message_text = message.text
    answer = get_related_words(message_text)
    bot.send_message(message.chat.id, answer)


if __name__ == '__main__':
    bot.infinity_polling()
    # bot.polling()
