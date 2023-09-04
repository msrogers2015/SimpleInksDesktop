import sqlite3
from gui import bases

class BaseCommands:
    def __init__(self, logged_user, menu):
        '''Initialize commands for base material window.'''
        # Create base material gui
        self.gui = bases.Bases(logged_user=logged_user, menu=menu)
        # Update buttons to utilize command codes.
        self.assign()
        # Mainloop to display and update window.
        self.gui.base_root.mainloop()
    
    def assign(self):
        '''Update buttons to assign commands for functionality.'''
        self.gui.edit_btn.config(command=lambda:self.edit_base())
    
    def edit_base(self):
        '''Edit material being displayed via enabling entry boxes.'''
        self.gui.alt_name_entry.config(state='normal')
        self.gui.description_entry.config(state='normal')
        self.gui.cost_entry.config(state='normal')
        self.gui.note_entry.config(state='normal')
        self.gui.vendor_entry.config(state='normal')
        self.gui.gal_lb_entry.config(state='normal')
        self.gui.low_inventory_entry.config(state='normal')
        self.gui.system_entry.config(state='normal')
        self.gui.search_entry.config(state='normal')
        self.gui.health_entry.config(state='normal')
        self.gui.flammability_entry.config(state='normal')
        self.gui.reactivity_entry.config(state='normal')
        self.gui.ppe_entry.config(state='normal')
        # Enable save button
        self.gui.save_btn.config(state='normal')
        #Disable all other buttons
        self.gui.edit_btn.config(state='disabled')
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
        pass