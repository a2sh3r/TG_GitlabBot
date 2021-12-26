import telebot #Библиотека с тг ботом
import gitlab


#Работа с гит лаб


user_name = ''
gitlabUrl= 'https://gitlab.com/'
token = 'glpat-cDC1Za7UVWJFmTcYhytJ'
projectId = 32387910
issue_title = []
closed_issue_title = []

gl = gitlab.Gitlab(gitlabUrl, token)
gl.auth()

botGit = telebot.TeleBot('5051671475:AAEPs3doUsurVa69iql8N_I1aBoPo5myNBs')  #токен

@botGit.message_handler(content_types=['text']) #декоратор для метода получения сообщений ботом

def start(message):
    if message.text == "/start":
        botGit.send_message(message.from_user.id, "Как тебя зовут?")
        botGit.register_next_step_handler(message, get_name)
    elif message.text=="/id":
        botGit.send_message(message.from_user.id, projectId)
        #botGit.send_message(message, list_issue)
    elif message.text=="/name":
        botGit.send_message(message.from_user.id, user_name)
    elif message.text=="/score":
        for issue in issue_title:
            botGit.send_message(message.from_user.id, issue)
    elif message.text=="/help":
        botGit.send_message(message.from_user.id, "/start - начало работы с ботом \n/score - показать проблемы \n/name - показать имя")
    else: 
        botGit.send_message(message.from_user.id,"Напиши /help")

    


def get_name (message):
    global user_name
    user_name = message.text
    botGit.send_message(message.from_user.id, 'Дай ссылку на свой репозиторий')
    botGit.register_next_step_handler(message, get_url)

def get_url(message):
    global projectId
    projectId = message.text

def list_issue():
    global issue_title
    global closed_issue_title
    project = gl.projects.get(projectId)
    issues = project.issues.list()
    closed_issues = gl.issues.list(state='closed')
    for issue in issues:
        issue_title.append(issue.title)
    for issue in closed_issues:
        closed_issue_title.append(issue.title)
    print(issue_title)
    print(closed_issue_title)

list_issue()

botGit.polling(none_stop=True, interval=0) #бот чекает пришло ли ему сообщение постоянно







