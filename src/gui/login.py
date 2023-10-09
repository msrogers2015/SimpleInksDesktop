import tkinter as tk
from tkinter import ttk
from functions import login_commands


class Login:
    title = ("Arial", 20)
    label = ("Arial", 16)
    button = ("Arial", 12)

    def __init__(self, database):
        """Create data for login window"""
        # Database name variable
        self.db = database
        # Window size variables
        self.width = 400
        self.height = 300

    def create_widgets(self):
        """Create window and widgets for login screen"""
        # Create window
        self.login_root = tk.Tk()
        # Link functions for login window
        self.commands = login_commands.LoginCommands(self.login_root, self.db)
        # Create window location variables
        self.x = int(
            self.login_root.winfo_screenwidth() / 2 - self.width / 2
        )
        self.y = int(
            self.login_root.winfo_screenheight() / 2 - self.height / 2
        )
        # Set up window geometery and location
        self.login_root.geometry(
            f"{self.width}x{self.height}+{self.x}+{self.y}"
        )
        # Rename window
        self.login_root.title("SimpleInks MS")
        # Create window widgets
        self.name = ttk.Label(
            self.login_root, text="SimpleInks MS", font=Login.title, anchor='center'
        )
        self.user_label = ttk.Label(
            self.login_root, text="Username", font=Login.label, anchor='center'
        )
        self.user_entry = ttk.Entry(
            self.login_root, font=Login.label, justify="center"
        )
        self.pass_label = ttk.Label(
            self.login_root, text="Password", font=Login.label, anchor='center'
        )
        self.pass_entry = ttk.Entry(
            self.login_root, font=Login.label, justify="center", show="*"
        )
        self.login = ttk.Button(
            self.login_root,
            text="Login",
            command=lambda: self.commands.login(
                self.user_entry.get(), self.pass_entry.get()
            ),
        )
        self.forgot_password = ttk.Button(
            self.login_root,
            text="Forgot Password",
            command=lambda: self.commands.forgot_password(),
        )
        self.version = ttk.Label(
            self.login_root, text="0.1.0a", font=Login.button
        )
        # Run function to place widgets and start main loop to display window
        self.place_widgets()
        self.login_root.mainloop()

    def place_widgets(self):
        """Place widgets within frame"""
        self.name.place(x=0, y=15, width=400, height=35)
        self.user_label.place(x=0, y=60, width=400, height=25)
        self.user_entry.place(x=50, y=85, width=300, height=40)
        self.pass_label.place(x=0, y=140, width=400, height=25)
        self.pass_entry.place(x=50, y=165, width=300, height=40)
        self.login.place(x=50, y=215, width=135, height=30)
        self.forgot_password.place(x=215, y=215, width=135, height=30)
        self.version.place(x=0, y=275, width=75, height=25)
