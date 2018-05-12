import logging
import telebot


logging.warning('Watch out!')  # will print a message to the console
logging.info('I told you so')  # will not print anything

access_token = '596275228:AAGyWbN1Nvs0BaMZFgf1ktNYjjh9iKyRRmE'
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)