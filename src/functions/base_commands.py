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

    def connect(self):
        self.con = sqlite3.connect(self.database)
        self.cur = self.con.cursor()

    def disconnect(self):
        self.con.close()

    def user_assignments(self):
        '''Enable and disable features based on user level.'''
        self.connect()
        sql = '''SELECT user_level FROM users WHERE employee_id = ?'''
        user_level = int(self.cur.execute(sql, (self.logged_user,)).fetchone()[0])
        self.disconnect()
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
        self.cur.execute(sql, values)
        self.con.commit()

    def load_bases(self):
        self.connect()
        '''Load a base from the database onto the screen.'''
        sql = '''SELECT * from bases'''
        self.data = self.cur.execute(sql).fetchall()
        self.disconnect()
        return self.data
    
    def populate_voc(self, base):
        self.connect()
        sql = '''SELECT voc, amount FROM base_voc WHERE base = ?'''
        voc_list = self.cur.execute(sql, (base,)).fetchall()
        self.disconnect()
        return voc_list
        
    def delete_voc(self, voc, base):
        try:
            sql = '''DELETE FROM base_voc WHERE base=? AND voc=?'''
            self.cur.execute(sql, (base, voc))
            return True
        except:
            return False