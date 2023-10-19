import requests
import os
import dotenv
from datetime import date, datetime
import logging
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'XKCDProject'))

from emailer import sendMail

def todoList(userID: str, apiKey: str):
    baseURL = "https://habitica.com/api/v3/tasks/user"
    headers = {"x-api-user": userID,
               "x-api-key": apiKey}

    response = requests.get(baseURL, headers=headers)
    response.raise_for_status()
    tasks = response.json()['data']

    todos = []
    for task in tasks:
        if task["type"] == "todo":
            todos.append(task)

    today = date.today()
    today = today.strftime("%d-%m-%Y")

    # Print the list of to-dos
    subject = "Today's to-do list"
    body = f'To-Do List {today}\n' + "-" * 30 + "\n"
    for todo in todos:
        body += f"Title: {todo['text']}\n"
        body += f"Notes: {todo['notes']}\n"
        body += f"Completed: {todo['completed']}\n"
        if 'date' in todo:  # Check if there's a due date
            dueDate = todo['date'].split('T')[0]  # Extract date portion
            dueDate = datetime.strptime(dueDate, "%Y-%m-%d")
            dueDate = dueDate.strftime("%d-%m-%Y")
            body += f"Due Date: {dueDate}\n"
        body += "-" * 30 + "\n"

    sendMail(subject, body)
    # print(body)

if __name__ == '__main__':
    api_key = os.getenv("HABITICA_API")
    userID = os.getenv("HABITICA_USERID")
    todoList(userID, api_key)