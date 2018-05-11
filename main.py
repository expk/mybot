# -*- coding: utf-8 -*-
import config
import telebot

bot = telebot.TeleBot(config.token)

#upd = bot.get_updates()
#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)


@bot.message_handler(content_types=['text'])
def handle_command(message):
    if message.text == "а":
        bot.send_message(message.chat.id, "Б")
    elif message.text == "б":
        bot.send_message(message.chat.id, "А")
    else:
        bot.send_message(message.chat.id, "Ты не умеешь играть в эту игру )))")
#    print("Пришёл текст")



bot.polling(none_stop=True, interval = 0)
