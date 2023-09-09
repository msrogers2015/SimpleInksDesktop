import sqlite3

# Level 1 is a vistor
# Level 2 is a tech
# Level 3 is a manager
# Level 4 is an admin

class BaseCommands:
    def __init__(self, logged_user):
        '''Initialize commands for base material window.'''
        self.database = "cims.db"
        self.logged_user = logged_user

    def user_assignments(self):
        '''Enable and disable features based on user level.'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = '''SELECT user_level FROM users WHERE employee_id = ?'''
        user_level = int(cur.execute(sql, (self.logged_user,)).fetchone()[0])
        con.close()
        return user_level
    
    def delete_base(self):
        pass

    def new_base(self):
        pass

    def use_report(self):
        pass

    def calculate_use(self):
        pass

    def rename_base(self):
        pass

    def print_base(self):
        pass

    def save_base(self, values):
        sql = '''UPDATE bases SET alt_name=?, lb_cost=?, health=?,
        flammable=?, reactive=?, ppe=?, warning_level=?, revision_version=?,
        notes=?, description=?, vendor=?, system=?, gallon_lb=? 
        WHERE base_name =?'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute(sql, values)
        con.commit()
        con.close()

    def load_bases(self):
        '''Load a base from the database onto the screen.'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = '''SELECT * from bases'''
        self.data = cur.execute(sql).fetchall()
        con.close()
        return self.data
    
    def populate_voc(self, base):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = '''SELECT voc, amount FROM base_voc WHERE base = ?'''
        voc_list = cur.execute(sql, (base,)).fetchall()
        con.close()
        return voc_list
        
