import sqlite3


class VocCommands:
    def __init__(self, logged_user, database):
        self.database = database
        self.logged_user = logged_user

    def connect(self):
        self.con = sqlite3.connect(self.database)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()
    
    def count_records(self):
        self.connect()
        sql = 'SELECT COUNT(*) FROM vocs'
        records = self.cur.execute(sql).fetchone()[0]
        self.disconnect()
        return records
    
    def fetch_record(self, index):
        if 0 <= index <= self.count_records():
            self.connect()
            sql = 'SELECT * FROM vocs LIMIT 1 OFFSET ?'
            record = self.cur.execute(sql, (index,)).fetchone()
            self.disconnect()
            return record
        else:
            return None

    def user_assignments(self):
        self.connect()
        sql = """SELECT user_level FROM users WHERE employee_id = ?"""
        user_level = int(
            self.cur.execute(sql, (self.logged_user,)).fetchone()[0])
        self.disconnect()
        return user_level

    def edit_record(self, data):
        self.connect()
        try:
            sql = """UPDATE vocs
            SET alt_name=?, formula=?,note=? WHERE voc=?"""
            self.cur.execute(sql, data)
            self.con.commit()
            self.disconnect()
            return [True, 0]
        except Exception as e:
            self.disconnect()
            return [False, e]

    def new_record(self, data):
        self.connect()
        try:
            sql = """INSERT INTO vocs VALUES(?,?,?,?)"""
            self.cur.execute(sql, data)
            self.con.commit()
            self.disconnect()
            return [True, 0]
        except Exception as e:
            self.disconnect()
            return [False, e]

    def delete_record(self, voc):
        self.connect()
        sql = """DELETE FROM vocs WHERE voc=?"""
        self.cur.execute(sql, (voc,))
        self.con.commit()
        self.disconnect()
