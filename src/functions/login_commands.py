import sqlite3
import hashlib
from gui import menu
from tkinter import messagebox

class LoginCommands:
    def __init__(self, login_window):
        self.window = login_window
        self.database = 'cims.db'

    def login(self, username, pword):
        salted_pword = username + '_' + pword
        hashed_pword = self.hash_password(bytes(salted_pword, 'utf-8'))
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = 'SELECT employee_id, pword from users WHERE employee_id=?'
        data = cur.execute(sql,(username,)).fetchone()
        if data == None:
            # Insert code for no information found
            print('User not found')
        if data != None:
            if data[1] == hashed_pword:
                self.menu = menu.Menu(username, self.window)
                self.menu.create_widgets()
            else:
                print('Wrong Password')
        con.close()
        
    def forgot_password(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        admins = []
        sql = '''SELECT first_name, last_name, user_level FROM users'''
        data = cur.execute(sql)
        for record in data.fetchall():
            fname, lname, level = record
            if level >= 3:
                admins.append(f'{fname} {lname}')
        message = f'Please contact one of the follow to reset your password: \n \n'
        for admin in admins:
            message += admin + '\n'
        messagebox.showinfo(title="Password Reset", message=message)

    def hash_password(self, pword):
        hashing = hashlib.sha256()
        hashing.update(pword)
        return hashing.hexdigest()
    