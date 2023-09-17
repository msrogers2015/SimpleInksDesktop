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
        sql = '''SELECT user_level FROM users WHERE employee_id = ?'''
        user_level = int(self.cur.execute(sql, (self.logged_user,)).fetchone()[0])
        self.disconnect()
        return user_level
    
    def load_vocs(self):
        self.connect()
        sql = '''SELECT * FROM vocs'''
        self.data = self.cur.execute(sql).fetchall()
        self.disconnect()
        return self.data

    def edit_record(self, data):
        try:
            self.connect()
            sql = '''UPDATE vocs SET alt_name=?, formula=?,note=? WHERE voc=?'''
            self.cur.execute(sql, data)
            self.con.commit()
            self.disconnect()
            return [True, 0]
        except Exception as e:
            return [False, e]

    def new_record(self, data):
        try:
            self.connect()
            sql = '''INSERT INTO vocs VALUES(?,?,?,?)'''
            self.cur.execute(sql, data)
            self.con.commit()
            self.disconnect()
            return [True, 0]
        except Exception as e:
            return [False, e]
    
    def delete_record(self, voc):
        self.connect()
        sql = '''DELETE FROM vocs WHERE voc=?'''
        self.cur.execute(sql, (voc,))
        self.con.commit()
        self.disconnect()