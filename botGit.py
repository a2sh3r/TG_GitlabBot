from os import close
import telebot #Библиотека с тг ботом, гитлабом и бдшками
import gitlab
import sqlite3

user_name = ''  #все переменные 
gitlabUrl= 'https://gitlab.com/'
token = 'glpat-Mw35Mruj-txxG71HLrKj'
projectId = 32385489
issue_title = []
closed_issue_title = []
open_date=[]
closed_open_date=[]
issue_state=[]
closed_issue_state=[]
issue_user = []
closed_issue_user = []
close_date=[]
closed_close_date=[]
gluser_list=[]

gl = gitlab.Gitlab(gitlabUrl, token)  #аутентификация гитлаба, для дальнейшей работы с проектами и issue
gl.auth()

botGit = telebot.TeleBot('5051671475:AAEPs3doUsurVa69iql8N_I1aBoPo5myNBs')  #токен

@botGit.message_handler(content_types=['text']) #декоратор для метода получения сообщений ботом

def start(message): #обработка сообщений ботом
    issue_title.clear()
    closed_issue_title.clear()
    issue_state.clear()
    close_date.clear()
    issue_user.clear()
    if message.text == "/start":
        botGit.send_message(message.from_user.id, "Как тебя зовут?")
        botGit.register_next_step_handler(message, get_name)
    elif message.text=="/id":
        botGit.register_next_step_handler(message, get_url)
    elif message.text=="/name":
        botGit.send_message(message.from_user.id, user_name)
    elif message.text=="/score":
        issue_title.clear()
        closed_issue_title.clear()
        issue_state.clear()
        close_date.clear()
        issue_user.clear()
        list_issue()
        i=0
        botGit.send_message(message.from_user.id, "Все Issue")
        for issue in issue_title:
            if issue_user[i]=='None':
                st=''.join(issue_user[i]) + " - " + ''.join(issue_title[i]) + " - " + ''.join(close_date[i]) + " - " + ''.join(issue_state[i])
            else: 
                st=', '.join(issue_user[i]) + " - " + ''.join(issue_title[i]) + " - " + ''.join(close_date[i]) + " - " + ''.join(issue_state[i])
            botGit.send_message(message.from_user.id, st)
            i=i+1
    elif message.text=="/nir":
        issue_title.clear()
        closed_issue_title.clear()
        issue_state.clear()
        close_date.clear()
        issue_user.clear()
        list_issue()
        i=0
        l=0
        botGit.send_message(message.from_user.id, "Закрытые Issue")
        while l<len(closed_issue_user):
            if l == user_name:
                print(closed_issue_user[l])
            if issue_user[i]=='None':
                st=''.join(closed_issue_user[i]) + " - " + ''.join(closed_issue_title[i]) + " - " + ''.join(closed_close_date[i]) 
            else: 
                st=', '.join(closed_issue_user[i]) + " - " + ''.join(closed_issue_title[i]) + " - " + ''.join(closed_close_date[i])
            botGit.send_message(message.from_user.id, st)
            i=i+1
            l=l+1
    elif message.text=="/help":
        botGit.send_message(message.from_user.id, "/start - начало работы с ботом \n/score - показать issue \n/id поменять айди проекта\n/nir вывод отфильтрованных данных по заданию")
    else: 
        botGit.send_message(message.from_user.id,"Напиши /help")

def get_name (message): #метод получения имени польщователя
    global user_name
    user_name = message.text
    botGit.send_message(message.from_user.id, 'Дай айди своего проекта')
    botGit.register_next_step_handler(message, get_url)

def get_url(message): #метод получения токена пользователя
    global projectId
    issue_title.clear()
    closed_issue_title.clear()
    issue_state.clear()
    close_date.clear()
    issue_user.clear()
    projectId = message.text
    


def list_issue(): #обработка и выдача информации по закрытым issue в проекте, указанном пользователем
    global issue_title
    global closed_issue_title
    global open_date
    global issue_state
    global close_date
    global issue_user
    global closed_open_date
    global closed_issue_state
    global closed_close_date
    global closed_issue_user
    assignees_name=[]
    closed_assignees_name=[]
    i=0
    k=0
    project = gl.projects.get(projectId)
    issues = project.issues.list()
    closed_issues = gl.issues.list(state='closed')
    for issue in issues:
        if issue.assignees:
            while (k<len(issue.assignees)):
                assignees_name.append(issue.assignees[k].get('name'))
                k=k+1
            issue_user.append(assignees_name)
        else:
            issue_user.append('None')
        issue_title.append(issue.title)   
        issue_state.append(issue.state)
        close_date.append(issue.updated_at)    
    
    for issue in issues:
        if issue.state=='closed':
            if issue.assignees:
                while (k<len(issue.assignees)):
                    closed_assignees_name.append(issue.assignees[k].get('name'))
                    k=k+1
                closed_issue_user.append(assignees_name)
            else:
                closed_issue_user.append('None')
            closed_issue_title.append(issue.title)   
            closed_issue_state.append(issue.state)
            closed_close_date.append(issue.updated_at)   

botGit.polling(none_stop=True, interval=0) #бот чекает пришло ли ему сообщение постоянно








