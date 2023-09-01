import sqlite3
import hashlib
from gui import menu

class LoginCommands:
    def __init__(self, login_window):
        self.window = login_window

    def login(self, username, pword):
        salted_pword = username + '_' + pword
        hashed_pword = self.hash_password(bytes(salted_pword, 'utf-8'))
        con = sqlite3.connect('cims.db')
        cur = con.cursor()
        sql = 'SELECT employee_id, pword from users WHERE employee_id=?'
        data = cur.execute(sql,(username,)).fetchone()
        if data == None:
            # Insert code for no information found
            print('User not found')
        if data != None:
            if data[1] == hashed_pword:
                self.menu = menu.Menu(username)
                self.menu.create_widgets()
                self.window.destroy()
            else:
                print('Wrong Password')
        con.close()
        
    def forgot_password(self):
        print('You forgot your password!')

    def hash_password(self, pword):
        hashing = hashlib.sha256()
        hashing.update(pword)
        return hashing.hexdigest()

if __name__ == '__main__':
    app = LoginCommands()
    pword = 'admin_admin'
    app.hash_password(bytes(pword,'utf-8' ))

