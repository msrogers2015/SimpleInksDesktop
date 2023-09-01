import os
import tkinter as tk
from functions import login_commands

class Login:
    title = ("Comic Sans MS", 20)
    label = ("Comic Sans MS", 16)
    button = ('Comic Sans MS', 12)
    def __init__(self):
        self.db = 'cims.db'
        self.root = tk.Tk()
        self.root.geometry('400x300')
        self.root.title('SimpleInks MS')
        self.commands = login_commands.LoginCommands(self.root)
        self.create_widgets()
        self.place_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.name = tk.Label(text='SimpleInks MS', font=Login.title)
        self.user_label = tk.Label(text='Username', font=Login.label)
        self.user_entry = tk.Entry(font=Login.label, justify='center')
        self.pass_label = tk.Label(text='Password', font=Login.label)
        self.pass_entry = tk.Entry(font=Login.label, justify='center', show='*')
        self.login = tk.Button(text='Login', justify='center', font=Login.button, command=lambda:self.commands.login(self.user_entry.get(), self.pass_entry.get()))
        self.forgot_password = tk.Button(text='Forgot Password', justify='center', font=Login.button, command=lambda:self.commands.forgot_password())
        self.version = tk.Label(text='0.1.0a',font=Login.button)

    def place_widgets(self):
        self.name.place(x=0,y=15,width=400,height=35)
        self.user_label.place(x=0,y=60,width=400,height=25)
        self.user_entry.place(x=50,y=85,width=300,height=40)
        self.pass_label.place(x=0,y=140,width=400,height=25)
        self.pass_entry.place(x=50,y=165,width=300,height=40)
        self.login.place(x=50,y=215,width=135,height=30)
        self.forgot_password.place(x=215,y=215,width=135,height=30)
        self.version.place(x=0,y=275,width=75,height=25)
    
if __name__ == "__main__":
    app = Login()
    app.create_widgets()
    app.place_widgets()
    app.root.mainloop()
