import sqlite3

# Level 1 is a visitor
# Level 2 is a tech
# Level 3 i

class VocCommands:
    def __init__(self, logged_user):
        self.database = 'cims.db'
        self.logged_user = logged_user
    
    def connect(self):
        self.con = sqlite3.connect(self.database)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def user_assignments(self):
        self.connect()
        sql = '''SELECT user_level FROM users WHERE employee_di = ?'''
        user_level = int(self.cur.execute(sql, (self.logged_user,)).fetchone()[0])
        self.disconnect()
        return user_level