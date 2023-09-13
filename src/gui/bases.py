import tkinter as tk
from tkinter import ttk, messagebox
from functions import base_commands as bc


class Bases:
    title = ("Comic Sans MS", 24)
    label = ("Comic Sans MS", 18)
    button = ("Comic Sans MS", 14)
    data = ("Comic Sans MS", 12)

    def __init__(self, logged_user, menu):
        """Initialize base window"""
        self.logged_user = logged_user
        self.width = 800
        self.height = 600
        self.menu = menu
        self.current_index = 0
        # Create connection to functions
        self.bc = bc.BaseCommands(logged_user=logged_user)
        self.data = self.bc.load_bases()
        self.total_records = len(self.data)
        # Hide menu window
        self.menu.withdraw()
        # Craete window for base materials
        self.create_window()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.place_widgets()
        self.voc_window()
        self.user_level()
        self.populate_base()
        # Display window
        self.base_root.mainloop()

    def create_window(self):
        """Create and configure window for bases."""
        self.base_root = tk.Tk()
        self.base_root.title("SimpleInks MS - Bases")
        self.x = int(self.base_root.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.base_root.winfo_screenheight() / 2 - self.height / 2)
        self.base_root.geometry(
            f"{self.width}x{self.height}+{self.x}+{self.y}"
        )
        # How to handle window closure.
        self.base_root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Create frame for VOCs
        self.voc_frame = tk.Frame(self.base_root, bg="green")
        self.voc_frame.place(x=390, y=115, width=400, height=150)

    def create_labels(self):
        """Create labels for base materials window"""
        self.title = tk.Label(
            self.base_root, text="Base Materials",
            font=Bases.title, justify="center"
        )
        self.name = tk.Label(
            self.base_root, text="Base Name",
            font=Bases.label, justify="center"
        )
        self.alt_name = tk.Label(
            self.base_root, text="Alternative Name",
            font=Bases.label, justify="center"
        )
        self.description = tk.Label(
            self.base_root, text="Description",
            font=Bases.label, justify="center"
        )
        self.cost = tk.Label(
            self.base_root, text="Cost",
            font=Bases.label, justify="center"
        )
        self.note = tk.Label(
            self.base_root, text="Quick Note",
            font=Bases.label, justify="center"
        )
        self.vendor = tk.Label(
            self.base_root, text="Vendor",
            font=Bases.label, justify="center"
        )
        self.gal_lb = tk.Label(
            self.base_root, text="Lbs. Per Gal",
            font=Bases.label, justify="center"
        )
        self.low_inventory = tk.Label(
            self.base_root,
            text="Low Inventory Level",
            font=Bases.label,
            justify="center",
        )
        self.system = tk.Label(
            self.base_root, text="Ink System",
            font=Bases.label, justify="center"
        )
        self.search = tk.Label(
            self.base_root, text="Search", font=Bases.label, justify="center"
        )
        self.health = tk.Label(
            self.base_root, text="Health", font=Bases.button, anchor="e"
        )
        self.flammability = tk.Label(
            self.base_root, text="Flammability", font=Bases.button, anchor="e"
        )
        self.reactivity = tk.Label(
            self.base_root, text="Reactivity", font=Bases.button, anchor="e"
        )
        self.ppe = tk.Label(self.base_root, text="PPE",
                            font=Bases.button, anchor="e"
                            )
        self.revision = tk.Label(
            self.base_root, text="Revision", font=Bases.button, anchor="e"
        )
        self.revision_version = tk.Label(
            self.base_root, text="00", font=Bases.button, anchor="w"
        )
        self.index = tk.Label(
            self.base_root, text='', font=Bases.button, justify='center'
        )

    def create_entries(self):
        """Create entry widgets"""
        self.base_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.alt_name_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.description_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.cost_entry = tk.Entry(self.base_root,
                                   font=Bases.data, state="disabled"
                                   )
        self.note_entry = tk.Entry(self.base_root,
                                   font=Bases.data, state="disabled"
                                   )
        self.vendor_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.gal_lb_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.low_inventory_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.system_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.search_entry = tk.Entry(
            self.base_root, font=Bases.data, state="normal"
        )
        self.health_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.flammability_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.reactivity_entry = tk.Entry(
            self.base_root, font=Bases.data, state="disabled"
        )
        self.ppe_entry = tk.Entry(self.base_root,
                                  font=Bases.data, state="disabled"
                                  )

    def create_buttons(self):
        """Create button widgets"""
        self.edit_btn = tk.Button(
            self.base_root, text="Edit Base", justify="center",
            font=Bases.button, command=lambda: self.edit_bases()
        )
        self.delete_btn = tk.Button(
            self.base_root, text="Delete Base", justify="center",
            font=Bases.button, command=lambda: self.delete()
        )
        self.new_btn = tk.Button(
            self.base_root, text="New Base", justify="center",
            font=Bases.button
        )
        self.report_btn = tk.Button(
            self.base_root, text="Useage Report", justify="center",
            font=Bases.button
        )
        self.usage_btn = tk.Button(
            self.base_root, text="Calculate Usage", justify="center",
            font=Bases.button
        )
        self.rename_btn = tk.Button(
            self.base_root, text="Rename Base", justify="center",
            font=Bases.button
        )
        self.print_btn = tk.Button(
            self.base_root, text="Print Base", justify="center",
            font=Bases.button
        )
        self.save_btn = tk.Button(
            self.base_root, text="Save Base", justify="center",
            font=Bases.button, state='disabled',
            command=lambda: self.save_record()
        )
        self.first_record_btn = tk.Button(
            self.base_root, text="<<", justify="center",
            font=Bases.button, command=lambda: self.first_record()
        )
        self.previous_record_btn = tk.Button(
            self.base_root, text="<", justify="center",
            font=Bases.button, command=lambda: self.previous_record()
        )
        self.next_record_btn = tk.Button(
            self.base_root, text=">", justify="center",
            font=Bases.button, command=lambda: self.next_record()
        )
        self.last_record_btn = tk.Button(
            self.base_root, text=">>", justify="center",
            font=Bases.button, command=lambda: self.last_record()
        )

    def voc_window(self):
            self.voc_frame = tk.Frame(self.base_root, bg='green')
            # Place frame
            self.voc_frame.place(x=390, y=115, width=400, height=150)
            # Treww view
            self.tree = ttk.Treeview(self.voc_frame)
            # Define columns
            self.tree['columns'] = ('Name','Amount')
            # Format columns
            self.tree.column('#0', width=50, minwidth=50)
            self.tree.column('Name', anchor='w', width=125, minwidth=125)
            self.tree.column('Amount', anchor='w', width=225, minwidth=225)
            # Crate headings or title labels
            self.tree.heading('#0', text='', anchor="w")
            self.tree.heading('Name', text='Name', anchor='w')
            self.tree.heading('Amount', text='Amount', anchor='w')           
            # Add table to window
            self.tree.pack()

    def place_widgets(self):
        """Place all widgets within the frame"""
        # Place labels
        self.title.place(x=200, y=0, width=400, height=40)
        self.name.place(x=10, y=35, width=340, height=30)
        self.alt_name.place(x=10, y=95, width=340, height=30)
        self.description.place(x=10, y=155, width=340, height=30)
        self.cost.place(x=10, y=240, width=340, height=30)
        self.note.place(x=10, y=300, width=340, height=30)
        self.vendor.place(x=10, y=360, width=340, height=30)
        self.gal_lb.place(x=10, y=420, width=340, height=30)
        self.low_inventory.place(x=10, y=480, width=340, height=30)
        self.system.place(x=10, y=540, width=340, height=30)
        self.search.place(x=400, y=35, width=390, height=30)
        self.health.place(x=465, y=510, width=125, height=25)
        self.flammability.place(x=630, y=510, width=125, height=25)
        self.reactivity.place(x=465, y=540, width=125, height=25)
        self.ppe.place(x=630, y=540, width=125, height=25)
        self.revision.place(x=570, y=570, width=125, height=25)
        self.revision_version.place(x=700, y=570, width=125, height=25)
        self.index.place(x=660, y=460, width=120, height=35)
        # Place entry
        self.base_entry.place(x=10, y=65, width=340, height=25)
        self.alt_name_entry.place(x=10, y=125, width=340, height=30)
        self.description_entry.place(x=10, y=185, width=340, height=50)
        self.cost_entry.place(x=10, y=270, width=340, height=30)
        self.note_entry.place(x=10, y=330, width=340, height=30)
        self.vendor_entry.place(x=10, y=390, width=340, height=30)
        self.gal_lb_entry.place(x=10, y=450, width=340, height=30)
        self.low_inventory_entry.place(x=10, y=510, width=340, height=30)
        self.system_entry.place(x=10, y=570, width=340, height=30)
        self.search_entry.place(x=400, y=65, width=390, height=30)
        self.health_entry.place(x=595, y=510, width=35, height=25)
        self.flammability_entry.place(x=760, y=510, width=35, height=25)
        self.reactivity_entry.place(x=595, y=540, width=35, height=25)
        self.ppe_entry.place(x=760, y=540, width=35, height=25)
        # Place Buttons
        self.edit_btn.place(x=420, y=280, width=175, height=35)
        self.delete_btn.place(x=605, y=280, width=175, height=35)
        self.new_btn.place(x=420, y=325, width=175, height=35)
        self.report_btn.place(x=605, y=325, width=175, height=35)
        self.usage_btn.place(x=420, y=370, width=175, height=35)
        self.rename_btn.place(x=605, y=370, width=175, height=35)
        self.print_btn.place(x=420, y=415, width=175, height=35)
        self.save_btn.place(x=605, y=415, width=175, height=35)
        self.first_record_btn.place(x=420, y=460, width=50, height=35)
        self.previous_record_btn.place(x=480, y=460, width=50, height=35)
        self.next_record_btn.place(x=540, y=460, width=50, height=35)
        self.last_record_btn.place(x=600, y=460, width=50, height=35)

    def on_close(self):
        '''How to handle window closure.'''
        # Destroy base materials and show menu window. 
        self.bc.disconnect()
        self.base_root.destroy()
        self.menu.deiconify()

    def edit_bases(self):
        if self.edit_btn.cget('text') == 'Edit Base':
            self.bc.connect()
            self.edit_btn.configure(text='Cancel')
            self.delete_btn.configure(text='Delete VOC')
            self.new_btn.configure(text='Add VOC')
            self.alt_name_entry.config(state='normal')
            self.description_entry.config(state='normal')
            self.cost_entry.config(state='normal')
            self.note_entry.config(state='normal')
            self.vendor_entry.config(state='normal')
            self.gal_lb_entry.config(state='normal')
            self.low_inventory_entry.config(state='normal')
            self.system_entry.config(state='normal')
            self.search_entry.config(state='disabled')
            self.health_entry.config(state='normal')
            self.flammability_entry.config(state='normal')
            self.reactivity_entry.config(state='normal')
            self.ppe_entry.config(state='normal')
            # Enable save button
            self.save_btn.config(state='normal')
            #Disable all other buttons
            self.report_btn.config(state='disabled')
            self.usage_btn.config(state='disabled')
            self.rename_btn.config(state='disabled')
            self.print_btn.config(state='disabled')
            self.first_record_btn.config(state='disabled')
            self.previous_record_btn.config(state='disabled')
            self.next_record_btn.config(state='disabled')
            self.last_record_btn.config(state='disabled')
        else:
            self.bc.disconnect()
            self.edit_btn.configure(text='Edit Base')
            self.delete_btn.config(text='Delete Base')
            self.new_btn.config(text='New Base')
            self.alt_name_entry.config(state='disabled')
            self.description_entry.config(state='disabled')
            self.cost_entry.config(state='disabled')
            self.note_entry.config(state='disabled')
            self.vendor_entry.config(state='disabled')
            self.gal_lb_entry.config(state='disabled')
            self.low_inventory_entry.config(state='disabled')
            self.system_entry.config(state='disabled')
            self.search_entry.config(state='normal')
            self.health_entry.config(state='disabled')
            self.flammability_entry.config(state='disabled')
            self.reactivity_entry.config(state='disabled')
            self.ppe_entry.config(state='disabled')
            # Enable save button
            self.save_btn.config(state='disabled')
            #Disable all other buttons
            self.report_btn.config(state='normal')
            self.usage_btn.config(state='normal')
            self.rename_btn.config(state='normal')
            self.print_btn.config(state='normal')
            self.first_record_btn.config(state='normal')
            self.previous_record_btn.config(state='normal')
            self.next_record_btn.config(state='normal')
            self.last_record_btn.config(state='normal')

    def user_level(self):
        level = self.bc.user_assignments()
        if level <= 2:
            self.edit_btn.config(state='disabled')
            self.new_btn.config(state='disabled')
            self.delete_btn.config(state='disabled')
            self.rename_btn.config(state='disabled')
        if level == 1:
            self.usage_btn.config(state='disabled')

    def populate_base(self):
        self.index.configure(text=f'{self.current_index+1}/{self.total_records}')
        base, alt, cost, health, flammable, reactive, ppe, warning, revision, \
        notes, description, vendor, system, gal = self.data[self.current_index]
        # Update Name
        self.base_entry.configure(state='normal')
        self.base_entry.delete(0, 'end')
        self.base_entry.insert(0, base)
        self.base_entry.configure(state='disable')
        # Update alternative name
        self.alt_name_entry.configure(state='normal')
        self.alt_name_entry.delete(0, 'end')
        self.alt_name_entry.insert(0, alt)
        self.alt_name_entry.configure(state='disable')
        # Update description
        self.description_entry.configure(state='normal')
        self.description_entry.delete(0, 'end')
        self.description_entry.insert(0, description)
        self.description_entry.configure(state='disable')
        # update cost
        self.cost_entry.configure(state='normal')
        self.cost_entry.delete(0, 'end')
        self.cost_entry.insert(0, cost)
        self.cost_entry.configure(state='disable')
        # Update note
        self.cost_entry.configure(state='normal')
        self.cost_entry.delete(0, 'end')
        self.cost_entry.insert(0, notes)
        self.cost_entry.configure(state='disable')
        # Update vendor
        self.vendor_entry.configure(state='normal')
        self.vendor_entry.delete(0, 'end')
        self.vendor_entry.insert(0, vendor)
        self.vendor_entry.configure(state='disable')
        # Update lbs
        self.gal_lb_entry.configure(state='normal')
        self.gal_lb_entry.delete(0, 'end')
        self.gal_lb_entry.insert(0, gal)
        self.gal_lb_entry.configure(state='disable')
        # Update inventory
        self.low_inventory_entry.configure(state='normal')
        self.low_inventory_entry.delete(0, 'end')
        self.low_inventory_entry.insert(0, warning)
        self.low_inventory_entry.configure(state='disable')
        # Update ink system
        self.system_entry.configure(state='normal')
        self.system_entry.delete(0, 'end')
        self.system_entry.insert(0, system)
        self.system_entry.configure(state='disable')
        # Update health
        self.health_entry.configure(state='normal')
        self.health_entry.delete(0, 'end')
        self.health_entry.insert(0, health)
        self.health_entry.configure(state='disable')
        # Update flammability
        self.flammability_entry.configure(state='normal')
        self.flammability_entry.delete(0, 'end')
        self.flammability_entry.insert(0, flammable)
        self.flammability_entry.configure(state='disable')
        # Update reactivity
        self.reactivity_entry.configure(state='normal')
        self.reactivity_entry.delete(0, 'end')
        self.reactivity_entry.insert(0, reactive)
        self.reactivity_entry.configure(state='disable')
        # Update PPE
        self.ppe_entry.configure(state='normal')
        self.ppe_entry.delete(0, 'end')
        self.ppe_entry.insert(0, ppe)
        self.ppe_entry.configure(state='disable')
        # Update revision
        self.revision_version.configure(text=revision)
        for voc in self.tree.get_children():
            self.tree.delete(voc)
        voc_list = self.bc.populate_voc(self.base_entry.get())
        for index, data in enumerate(voc_list):
            voc, amount = data
            self.tree.insert(parent='', index='end', iid=index+1,
                                 text=str(index+1), values=(voc, amount))
            
    def next_record(self):
        if self.current_index != self.total_records - 1:
            self.current_index += 1
            self.populate_base()
    
    def previous_record(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.populate_base()
    
    def first_record(self):
        self.current_index = 0
        self.populate_base()
    
    def last_record(self):
        self.current_index = self.total_records - 1
        self.populate_base()

    def save_record(self):
        try:
            values = [
                self.alt_name_entry.get(),
                self.cost_entry.get(),
                self.health_entry.get(),
                self.flammability_entry.get(),
                self.reactivity_entry.get(),
                self.ppe_entry.get(),
                self.low_inventory_entry.get(),
                int(self.revision_version.cget('text')) + 1,
                self.note_entry.get(),
                self.description_entry.get(),
                self.vendor_entry.get(),
                self.system_entry.get(),
                self.gal_lb_entry.get(),
                self.base_entry.get(),
            ]
            self.bc.save_base(values)
            self.data = self.bc.load_bases()
            self.populate_base()
            self.edit_bases()
        except ValueError:
            messagebox.showerror(title='Value Error',
                                 message='Please check all information.')

    def delete(self):
        if self.delete_btn.cget('text') == 'Delete Base':
            pass
        else:
            selected_voc = self.tree.item(self.tree.focus())['values'][0]
            status = self.bc.delete_voc(selected_voc, self.base_entry.get())
            if status:
                deleted_voc = self.tree.selection()[0]
                self.tree.delete(deleted_voc)

    def add(self):
        pass
