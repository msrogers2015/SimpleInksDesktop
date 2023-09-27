import sqlite3
from functions import voc_commands as vc

class VocTests:
    def __init__(self):
        '''Format the database for testing'''
        # Create connection to commands for testing
        self.vc = vc.VocCommands()
        # Change database to testing database
        self.vc.database = 'test.db'
        # Connect to database
        self.vc.connect()
        # Empty tanles
        self.vc.cur.execute('''DELETE FROM vocs''')
        self.vc.cur.execute('''DELETE FROM users''')
        # Add four new records for testing
        for i in range(1,5,1):
            values = (f'VOC {i}',f'Name {i}',f'Formula {i}',f'Note {i}')
            self.vc.cur.execute('''INSERT INTO vocs VALUES(?,?,?,?)''', values)
        # Add four users for testing
        for x in range(1,5,1):
            e_values = (f'id_{x}', f'Employee {x}', 'Doe', 'Test', x,
                      f'employee{x}.doe@company.xyz')
            self.vc.cur.execute('''INSERT INTO users VALUES(?,?,?,?,?,?)''',
                                e_values)
        # Save changes and close database connectino
        self.vc.con.commit()
        self.vc.con.close()
        self.vc.disconnect()
    
    def check_connection(self):
        '''Test connecting to database'''
        print('Testing database connection.')
        # Connection should be closed and return an exception
        try:
            self.vc.cur.execute('SELECT * FROM vocs')
            print('No connection: Failed')
        except Exception:
            print('No connection: Passed')
        self.vc.connect()
        # Databse should be connected and query database with no issue
        try:
            self.vc.cur.execute('SELECT * FROM vocs')
            print('Connection: Passed')
        except Exception:
            print('Connection: Failed')

    def check_disconnect(self):
        '''Test disconnecting from database.'''
        print('Testing database closure.')
        # Database should be open and able to query
        try:
            self.vc.cur.execute('SELECT * FROM vocs')
            print('Not Closed: Passed')
        except Exception:
            print('Not Closed: Failed')
        self.vc.disconnect()
        # Database should be closed and return an exception.
        try:
            self.vc.cur.execute('SELECT * FROM vocs')
            print('Closure: Failed')
        except Exception:
            print('Closure: Passed')
        
    def check_count(self):
        '''Check count record function.'''
        # Count should return 4 records.
        if self.vc.count_records() == 4:
            print('Count Records: Passed')
        else:
            print('Count Records: Failed')
    
    def check_fetch(self):
        '''Check retriving single record.'''
        print('Testing record retrival.')
        pass_ = 0
        fail_ = 0
        # Loop through 6 records ranging from index of -1 to 4
        for x in range(-1, 5, 1):
            # let x be the index and i be the record number
            i = x + 1
            values = (f'VOC {i}',f'Name {i}',f'Formula {i}',f'Note {i}')
            # If index is within the range of total records, check values
            if 0 <= x < 4:
                # Increase pass value if records match expected results.
                if self.vc.fetch_record(x) == values:
                    pass_ += 1
            # Check if index is too high or negative
            elif x == -1 or x == 4:
                # Expect "None" to be returned
                if self.vc.fetch_record(x) == None:
                    pass_ += 1
            # If all else fails, increase fail counter
            else: fail_ += 1
        print(f'Fetch Results: {pass_}/{pass_ + fail_} passed')
    
    def check_users(self):
        '''Check user level assignments.'''
        print('Testing user assignments.')
        pass_ = 0
        fail_ = 0
        # Loop through total number of records
        for x in range(1, 5, 1):
            # Update logged user as this is a variable pass through the software
            self.vc.logged_user = f'id_{x}'
            # User level should match user index
            if self.vc.user_assignments() == x:
                pass_ += 1
            else:
                fail_ += 1
        print(f'User Assignment Results: {pass_}/{pass_ + fail_} passed')
    
    def check_edit(self):
        '''Check editing and updateing records.'''
        print('Testing Record Editing.')
        # Create edit data tuple
        data = ('Hydrogen Monoxide','H2O', 'Water', 'VOC 1')
        results = self.vc.edit_record(data)
        # Function returns a two item list, if first item is True, record has 
        # been updated. If first item is False, there should be an exception
        if results[0]:
            if self.vc.fetch_record(0) == ('VOC 1', 'Hydrogen Monoxide','H2O', 'Water'):
                print('Record update passed')
            else:
                print('Record update failed')
        if not results[0]:
            print(f'Edit failed: {results[1]}')
    
    def check_add(self):
        '''Checking the addition of a new record into database.'''
        print('Testing new record.')
        # Create a tuple of new data and a tuple of existing data
        data = ('Hydrogen Peroxide', '', 'H2O2','Do not Drink!')
        data2 = ('VOC 1', 'Hydrogen Monoxide','H2O', 'Water')
        result1 = self.vc.new_record(data)
        result2 = self.vc.new_record(data2)
        # New data should return a True as the first item of the list.
        if result1[0]:
            print('New record added')
        else:
            print(f'New Record failed: {result1[1]}')
        # Existing data should return a False and exeption for the list.
        if not result2[0]:
            print(f'Passed with error:{result2[1]}')
        else:
            print('New record failed: record exist.')
    
    def check_delete(self):
        '''Check if vocs are deleted from database.'''
        print('Testing record deletion.')
        # Delete record with id VOC 1
        self.vc.delete_record('VOC 1')
        # Check if record has been deleted
        self.vc.connect()
        record = self.vc.cur.execute("""SELECT * FROM vocs WHERE voc='VOC 1'""").fetchone()
        # Expect a non value as the query shouldn't return data.
        if record == None:
            print('Successfully deleted record.')
        else:
            print('Deletion failed.')
        self.vc.disconnect()