import sqlite3
from gui import bases

# Level 1 is a vistor
# Level 2 is a tech
# Level 3 is a manager
# Level 4 is an admin

class BaseCommands:
    def __init__(self, logged_user, menu):
        '''Initialize commands for base material window.'''
        self.database = "cims.db"
        self.logged_user = logged_user
        self.current_index = 0
        # Create base material gui
        self.gui = bases.Bases(logged_user=logged_user, menu=menu)
        # Update buttons to utilize command codes.
        self.assign()
        self.user_assignments()
        # Retrieve and populate first base
        self.load_base()
        self.populate_base(self.current_index)
        # Mainloop to display and update window.
        self.gui.base_root.mainloop()

    def user_assignments(self):
        '''Enable and disable features based on user level.'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = '''SELECT user_level FROM users WHERE employee_id = ?'''
        user_level = int(cur.execute(sql, (self.logged_user,)).fetchone()[0])
        if user_level == 1:
            self.gui.edit_btn.config(state='disabled')
            self.gui.new_btn.config(state='disabled')
            self.gui.delete_btn.config(state='disabled')
            self.gui.usage_btn.config(state='disabled')
            self.gui.rename_btn.config(state='disabled')
        if user_level == 2:
            self.gui.edit_btn.config(state='disabled')
            self.gui.new_btn.config(state='disabled')
            self.gui.delete_btn.config(state='disabled')
            self.gui.rename_btn.config(state='disabled')
    
    def assign(self):
        '''Update buttons to assign commands for functionality.'''
        self.gui.edit_btn.config(command=lambda:self.edit_base())
        self.gui.save_btn.config(command=lambda:self.save_base())
        self.gui.next_record_btn.config(command=lambda: self.next_record())
        self.gui.previous_record_btn.config(
            command=lambda:self.previous_record()
        )
        self.gui.last_record_btn.config(command=lambda: self.last_record())
        self.gui.first_record_btn.config(command=lambda: self.first_record())
    
    def edit_base(self):
        '''Edit material being displayed via enabling entry boxes.'''
        if self.gui.edit_btn.cget('text') == 'Edit Base':
            self.gui.edit_btn.configure(text='Cancel')
            self.gui.alt_name_entry.config(state='normal')
            self.gui.description_entry.config(state='normal')
            self.gui.cost_entry.config(state='normal')
            self.gui.note_entry.config(state='normal')
            self.gui.vendor_entry.config(state='normal')
            self.gui.gal_lb_entry.config(state='normal')
            self.gui.low_inventory_entry.config(state='normal')
            self.gui.system_entry.config(state='normal')
            self.gui.search_entry.config(state='disabled')
            self.gui.health_entry.config(state='normal')
            self.gui.flammability_entry.config(state='normal')
            self.gui.reactivity_entry.config(state='normal')
            self.gui.ppe_entry.config(state='normal')
            # Enable save button
            self.gui.save_btn.config(state='normal')
            #Disable all other buttons
            self.gui.delete_btn.config(state='disabled')
            self.gui.new_btn.config(state='disabled')
            self.gui.report_btn.config(state='disabled')
            self.gui.usage_btn.config(state='disabled')
            self.gui.rename_btn.config(state='disabled')
            self.gui.print_btn.config(state='disabled')
            self.gui.first_record_btn.config(state='disabled')
            self.gui.previous_record_btn.config(state='disabled')
            self.gui.next_record_btn.config(state='disabled')
            self.gui.last_record_btn.config(state='disabled')
        else:
            self.gui.edit_btn.configure(text='Edit Base')
            self.gui.alt_name_entry.config(state='disabled')
            self.gui.description_entry.config(state='disabled')
            self.gui.cost_entry.config(state='disabled')
            self.gui.note_entry.config(state='disabled')
            self.gui.vendor_entry.config(state='disabled')
            self.gui.gal_lb_entry.config(state='disabled')
            self.gui.low_inventory_entry.config(state='disabled')
            self.gui.system_entry.config(state='disabled')
            self.gui.search_entry.config(state='normal')
            self.gui.health_entry.config(state='disabled')
            self.gui.flammability_entry.config(state='disabled')
            self.gui.reactivity_entry.config(state='disabled')
            self.gui.ppe_entry.config(state='disabled')
            # Enable save button
            self.gui.save_btn.config(state='disabled')
            #Disable all other buttons
            self.gui.edit_btn.config(state='normal')
            self.gui.delete_btn.config(state='normal')
            self.gui.new_btn.config(state='normal')
            self.gui.report_btn.config(state='normal')
            self.gui.usage_btn.config(state='normal')
            self.gui.rename_btn.config(state='normal')
            self.gui.print_btn.config(state='normal')
            self.gui.first_record_btn.config(state='normal')
            self.gui.previous_record_btn.config(state='normal')
            self.gui.next_record_btn.config(state='normal')
            self.gui.last_record_btn.config(state='normal')

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

    def save_base(self):
        base = self.gui.base_entry.get()
        alt_name = self.gui.alt_name_entry.get()
        description = self.gui.description_entry.get()
        cost = self.gui.cost_entry.get()
        note = self.gui.note_entry.get()
        vendor = self.gui.vendor_entry.get()
        gal = self.gui.gal_lb_entry.get()
        inv = self.gui.low_inventory_entry.get()
        system = self.gui.system_entry.get()
        health = self.gui.health_entry.get()
        flame = self.gui.flammability_entry.get()
        react = self.gui.reactivity_entry.get()
        ppe = self.gui.ppe_entry.get()
        revision = int(self.gui.revision_version.cget('text')) + 1
        sql = '''UPDATE bases SET alt_name=?, lb_cost=?, health=?,
        flammable=?, reactive=?, ppe=?, warning_level=?, revision_version=?,
        notes=?, description=?, vendor=?, system=?, gallon_lb=? 
        WHERE base_name =?'''
        values = (alt_name, cost, health, flame, react, ppe, inv, revision,
                  note, description, vendor, system, gal, base)
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        cur.execute(sql, values)
        con.commit()
        con.close()
        self.load_base()
        self.populate_base(self.current_index)

        self.edit_base()

    def load_base(self):
        '''Load a base from the database onto the screen.'''
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = '''SELECT * from bases'''
        self.data = cur.execute(sql).fetchall()
        con.close()
    
    def populate_base(self, index):
        '''Update entries with base information.'''
        total_records = len(self.data)
        self.gui.index.config(text=f'{self.current_index+1}/{total_records}')
        base, alt, cost, health, flammable, reactive, ppe, warning, revision, \
        notes, description, vendor, system, gal = self.data[index]
        # Update Name
        self.gui.base_entry.configure(state='normal')
        self.gui.base_entry.delete(0, 'end')
        self.gui.base_entry.insert(0, base)
        self.gui.base_entry.configure(state='disable')
        # Update alternative name
        self.gui.alt_name_entry.configure(state='normal')
        self.gui.alt_name_entry.delete(0, 'end')
        self.gui.alt_name_entry.insert(0, alt)
        self.gui.alt_name_entry.configure(state='disable')
        # Update description
        self.gui.description_entry.configure(state='normal')
        self.gui.description_entry.delete(0, 'end')
        self.gui.description_entry.insert(0, description)
        self.gui.description_entry.configure(state='disable')
        # update cost
        self.gui.cost_entry.configure(state='normal')
        self.gui.cost_entry.delete(0, 'end')
        self.gui.cost_entry.insert(0, cost)
        self.gui.cost_entry.configure(state='disable')
        # Update note
        self.gui.cost_entry.configure(state='normal')
        self.gui.cost_entry.delete(0, 'end')
        self.gui.cost_entry.insert(0, cost)
        self.gui.cost_entry.configure(state='disable')
        # Update vendor
        self.gui.vendor_entry.configure(state='normal')
        self.gui.vendor_entry.delete(0, 'end')
        self.gui.vendor_entry.insert(0, vendor)
        self.gui.vendor_entry.configure(state='disable')
        # Update lbs
        self.gui.gal_lb_entry.configure(state='normal')
        self.gui.gal_lb_entry.delete(0, 'end')
        self.gui.gal_lb_entry.insert(0, gal)
        self.gui.gal_lb_entry.configure(state='disable')
        # Update inventory
        self.gui.low_inventory_entry.configure(state='normal')
        self.gui.low_inventory_entry.delete(0, 'end')
        self.gui.low_inventory_entry.insert(0, warning)
        self.gui.low_inventory_entry.configure(state='disable')
        # Update ink system
        self.gui.system_entry.configure(state='normal')
        self.gui.system_entry.delete(0, 'end')
        self.gui.system_entry.insert(0, system)
        self.gui.system_entry.configure(state='disable')
        # Update health
        self.gui.health_entry.configure(state='normal')
        self.gui.health_entry.delete(0, 'end')
        self.gui.health_entry.insert(0, health)
        self.gui.health_entry.configure(state='disable')
        # Update flammability
        self.gui.flammability_entry.configure(state='normal')
        self.gui.flammability_entry.delete(0, 'end')
        self.gui.flammability_entry.insert(0, flammable)
        self.gui.flammability_entry.configure(state='disable')
        # Update reactivity
        self.gui.reactivity_entry.configure(state='normal')
        self.gui.reactivity_entry.delete(0, 'end')
        self.gui.reactivity_entry.insert(0, reactive)
        self.gui.reactivity_entry.configure(state='disable')
        # Update PPE
        self.gui.ppe_entry.configure(state='normal')
        self.gui.ppe_entry.delete(0, 'end')
        self.gui.ppe_entry.insert(0, ppe)
        self.gui.ppe_entry.configure(state='disable')
        # Update revision
        self.gui.revision_version.configure(text=revision)
        for voc in self.gui.tree.get_children():
            self.gui.tree.delete(voc)
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        sql = '''SELECT voc, amount from base_voc where base = ?'''
        voc_list = cur.execute(sql, (base,))
        for index, data in enumerate(voc_list):
            voc, amount = data
            self.gui.tree.insert(parent='', index='end', iid=index+1,
                                 text=str(index+1), values=(voc, amount))
            
    def next_record(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        data = cur.execute('''SELECT * FROM bases''').fetchall()
        con.close()
        if self.current_index + 1 < len(data):
            self.current_index += 1
            self.populate_base(self.current_index)

    def previous_record(self):
        if self.current_index != 0:
            self.current_index -= 1
            self.populate_base(self.current_index)
    
    def last_record(self):
        con = sqlite3.connect(self.database)
        cur = con.cursor()
        data = cur.execute('''SELECT * FROM bases''').fetchall()
        con.close()
        self.current_index = len(data)-1
        self.populate_base(self.current_index)

    def first_record(self):
        self.current_index = 0
        self.populate_base(self.current_index)
