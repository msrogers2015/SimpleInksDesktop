import sqlite3
from tkinter import messagebox

class BaseCommands:
    def __init__(self, logged_user, database):
        '''Initialize commands for base material window'''
        self.database = database
        self.logged_user = logged_user

    def connect(self):
        self.con = sqlite3.connect(self.database)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()
    
    def user_assignments(self) -> int:
        '''Enable and disable features based on user level.'''
        self.connect()
        sql = '''SELECT user_level FROM users WHERE employee_id = ?'''
        user_level = int(self.cur.execute(sql, (self.logged_user,)).fetchone()[0])
        self.disconnect()
        return user_level
    
    def populate_voc(self, base: str) -> list:
        self.connect()
        sql = '''SELECT voc, amount FROM base_voc WHERE base = ?'''
        voc_list = self.cur.execute(sql, (base,)).fetchall()
        self.disconnect()
        return voc_list
    
    def delete_base(self, base: str):
        self.connect()
        sql = '''DELETE FROM bases WHERE base_name = ?'''
        self.cur.execute(sql, (base,))
        self.con.commit()
        self.disconnect()

    def count_bases(self) -> int:
        self.connect()
        sql = '''SELECT COUNT(base_name) FROM bases'''
        count = self.cur.execute(sql).fetchone()[0]
        self.disconnect()
        return count
    
    def get_base(self, index: int) -> list:
        self.connect()
        sql = '''SELECT * FROM bases ORDER BY base_name ASC LIMIT 1 OFFSET ?'''
        record = self.cur.execute(sql, (index,)).fetchone()
        self.disconnect()
        return record
    
    def delete_voc(self, base: str, voc: str) -> bool:
        try:
            sql = '''DELETE from base_voc WHERE base=? and voc=?'''
            self.cur.execute(sql, (base, voc))
            return True
        except Exception as e:
            print(e)
            return False
        
    def save_base(self, values: list):
        sql = '''UPDATE bases SET alt_name=?, lb_cost=?, health=?,
        flammable=?, reactive=?, ppe=?, warning_level=?, revision_version=?,
        notes=?, description=?, vendor=?, system=?, gallon_lb=? 
        WHERE base_name =?'''
        self.cur.execute(sql, values)
        self.con.commit()
        self.disconnect()

    def new_base(self, values: list):
        sql = '''INSERT INTO bases (alt_name, lb_cost, health, flammable,
        reactive, ppe, warning_level, revision_version, notes, description,
        vendor, system, gallon_lb, base_name)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
        try:
            self.cur.execute(sql, values)
        except Exception as e:
            messagebox.showerror(
                title='Error saving',
                message=e
            )
        self.con.commit()
        self.disconnect()

    def use_report(self, base: str):
        pass

    def calculate_use(self, base: str):
        pass

    def rename_base(self, base: str):
        pass

    def print_base(self, base: str):
        pass

    def voc_list(self) -> list:
        self.connect()
        voc_list = self.cur.execute('''SELECT voc FROM vocs''').fetchall()
        self.disconnect()
        return voc_list
