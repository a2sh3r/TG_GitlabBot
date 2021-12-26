import telebot #Библиотека с тг ботом
botGit = telebot.TeleBot('5051671475:AAEPs3doUsurVa69iql8N_I1aBoPo5myNBs')  #токен

@botGit.message_handler(content_types=['text']) #декоратор для метода получения сообщений ботом
def get_text_messages(message):
    if message.text == "/start":
        botGit.send_message(message.from_user.id, "Салам, для начала работы поздоровайтесь со мной, но только козырно)")
    elif message.text == "Салам":
        botGit.send_message(message.from_user.id, "Чем могу быть полезен, сударь?")
    elif message.text == "/help":
        botGit.send_message(message.from_user.id, "Напиши Салам")
    else:
        botGit.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    
botGit.polling(none_stop=True, interval=0) #бот чекает пришло ли ему сообщение постоянно



