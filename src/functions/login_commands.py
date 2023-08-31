import sqlite3
import os

class LoginCommands:
    def __init__(self):
        print("Login Commands")
        print(os.getcwd())

    def login(self, username, pword):
        print(username, pword)
        
    def forgot_password(self):
        print('You forgot your password!')

