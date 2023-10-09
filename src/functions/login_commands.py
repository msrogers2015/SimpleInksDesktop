import sqlite3
import hashlib
from gui import menu
from tkinter import messagebox


class LoginCommands:
    def __init__(self, login_window, database):
        """Iniital commands for login window"""
        self.window = login_window
        self.database = database

    def login(self, username, pword):
        """Check user data and display menu."""
        # Hash password with salt so password is never saved
        hashed_pword = self.hash_password(
            bytes(username + "_" + pword, "utf-8")
        )
        # Connect to database and create cursor for navigation
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        # SQL Code and grab data
        sql = "SELECT employee_id, pword from users WHERE employee_id=?"
        data = cur.execute(sql, (username,)).fetchone()
        # Close database connection
        con.close()
        if data is None:
            # Display warning if missing information.
            messagebox.showwarning(
                title="User Not Found",
                message=f"User {username} couldn't be found."
            )
        if data is not None:
            if data[1] == hashed_pword:
                # If password matches stored hash, display menu and destroy
                # login window
                self.menu = menu.Menu(username, self.window, self.database)
                self.menu.create_widgets()
            else:
                # If password doesn't match, show error message
                messagebox.showerror(
                    title="Incorrect Password",
                    message="Password is incorrect."
                )

    def forgot_password(self):
        """Display information for resettings password."""
        # Connect to database and create cursor
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        # Create list to hold managers and admins
        admins = []
        # SQL code and execute it
        sql = """SELECT first_name, last_name, user_level FROM users"""
        data = cur.execute(sql)
        for record in data.fetchall():
            # Loop through users and add managers and admins to list.
            fname, lname, level = record
            if level >= 3:
                admins.append(f"{fname} {lname}")
        # Build info message for list of users who can reset passwords.
        message = "Please contact one of the follow to reset your " \
            "password: \n \n"
        for admin in admins:
            message += "-" + admin + "\n"
        # Display list of users that can reset passwords.
        messagebox.showinfo(title="Password Reset", message=message)

    def hash_password(self, pword):
        """Password hashing function for password protection."""
        hashing = hashlib.sha256()
        hashing.update(pword)
        return hashing.hexdigest()
