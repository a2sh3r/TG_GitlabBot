import telebot #Библиотека с тг ботом
import gitlab
import csv


#Работа с гит лаб


gitlabUrl= 'https://gitlab.com/'
token = 'glpat-cDC1Za7UVWJFmTcYhytJ'
projectId = 32385489


gl = gitlab.Gitlab(gitlabUrl, token)
gl.auth()

project = gl.projects.get(projectId)
issues = project.issues.list()
for issue in issues:
        print (issue.iid)


botGit = telebot.TeleBot('5051671475:AAEPs3doUsurVa69iql8N_I1aBoPo5myNBs')  #токен


repName = ''
user_name = ''



@botGit.message_handler(content_types=['text']) #декоратор для метода получения сообщений ботом

def start(message):
    if message.text == "/start":
        botGit.send_message(message.from_user.id, "Как тебя зовут?")
        botGit.register_next_step_handler(message, get_name)
    elif message.text=="/url":
        botGit.send_message(message.from_user.id, repName)
    elif message.text=="/name":
        botGit.send_message(message.from_user.id, user_name)
    elif message.text=="/help":
        botGit.send_message(message.from_user.id, "/start - начало работы с ботом \n/url - показать ссылку на репозиторий \n/name - показать имя")
    else: 
        botGit.send_message(message.from_user.id,"Напиши /help")
    


def get_name (message):
    global user_name
    user_name = message.text
    botGit.send_message(message.from_user.id, 'Дай ссылку на свой репозиторий')
    botGit.register_next_step_handler(message, get_url)

def get_url(message):
    global repName
    repName = message.text

botGit.polling(none_stop=True, interval=0) #бот чекает пришло ли ему сообщение постоянно







