import telebot #Библиотека с тг ботом, гитлабом и бдшками
import gitlab
import sqlite3

user_name = ''  #все переменные 
gitlabUrl= 'https://gitlab.com/'
token = 'glpat-cDC1Za7UVWJFmTcYhytJ'
projectId = 32387910
issue_title = []
closed_issue_title = []
gluser_list=[]

gl = gitlab.Gitlab(gitlabUrl, token)  #аутентификация гитлаба, для дальнейшей работы с проектами и issue
gl.auth()

botGit = telebot.TeleBot('5051671475:AAEPs3doUsurVa69iql8N_I1aBoPo5myNBs')  #токен

@botGit.message_handler(content_types=['text']) #декоратор для метода получения сообщений ботом

def start(message): #обработка сообщений ботом
    if message.text == "/start":
        botGit.send_message(message.from_user.id, "Как тебя зовут?")
        botGit.register_next_step_handler(message, get_name)
    elif message.text=="/id":
        botGit.register_next_step_handler(message, get_id)
    elif message.text=="/name":
        botGit.send_message(message.from_user.id, user_name)
    elif message.text=="/score":
        for issue in issue_title:
            botGit.send_message(message.from_user.id, issue)
    elif message.text=="/help":
        botGit.send_message(message.from_user.id, "/start - начало работы с ботом \n/score - показать issue \n/id поменять айди проекта")
    else: 
        botGit.send_message(message.from_user.id,"Напиши /help")

def get_name (message): #метод получения имени польщователя
    global user_name
    user_name = message.text
    botGit.send_message(message.from_user.id, 'Дай айди своего проекта')
    botGit.register_next_step_handler(message, get_url)

def get_url(message): #метод получения токена пользователя
    global projectId
    projectId = message.text
    list_issue()

def get_id(message): #метод получения токена пользователя
    global projectId, issue_title, closed_issue_title
    issue_title.clear()
    closed_issue_title.clear()
    projectId = message.text
    list_issue()

def list_issue(): #обработка и выдача информации по закрытым issue в проекте, указанном пользователем
    global issue_title
    global closed_issue_title
    project = gl.projects.get(projectId)
    issues = project.issues.list()
    closed_issues = gl.issues.list(state='closed')
    for issue in issues:
        issue_title.append(issue.title)
    for issue in closed_issues:
        closed_issue_title.append(issue.title)

botGit.polling(none_stop=True, interval=0) #бот чекает пришло ли ему сообщение постоянно







