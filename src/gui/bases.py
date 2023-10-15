import tkinter as tk
from tkinter import ttk, messagebox
from functions import base_commands


class Bases:
    title = ('Arial', 24)
    label = ('Arial', 18)
    button = ('Arial', 14)
    data = ('Arial', 12)

    def __init__(self, logged_user, menu, database):
        '''Initialze Base Window.'''
        self.logged_user = logged_user
        self.menu = menu
        self.state = None
        self.commands = base_commands.BaseCommands(logged_user, database)
        # Hide main menu
        self.menu.withdraw()
        # Create variables
        self.current_index = 0
        self.voc_index = 0
        self.create_window()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.place_widgets()
        self.create_table()
        self.populate_base()
        self.user_level()
        self.root.mainloop()

    def create_window(self):
        '''Create and configure window for bases.'''
        self.root = tk.Tk()
        self.root.title('SimpleInks MS - Bases')
        self.width = 800
        self.height = 615
        swidth = self.root.winfo_screenwidth()
        sheight = self.root.winfo_screenheight()
        x = int(swidth/2 - self.width/2)
        y = int(sheight/2 - self.height/2)
        self.root.geometry(f'{self.width}x{self.height}+{x}+{y}')
        # Handling the close button
        self.root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.root.bind('<Control-p>',self.print_vocs)

    def create_labels(self):
        """Create labels for base materials window"""
        self.title = ttk.Label(
            self.root, text="Base Materials",
            font=Bases.title, anchor="center"
        )
        self.name = ttk.Label(
            self.root, text="Base Name",
            font=Bases.label, anchor="center"
        )
        self.alt_name = ttk.Label(
            self.root, text="Alternative Name",
            font=Bases.label, anchor="center"
        )
        self.description = ttk.Label(
            self.root, text="Description",
            font=Bases.label, anchor="center"
        )
        self.cost = ttk.Label(
            self.root, text="Cost",
            font=Bases.label, anchor="center"
        )
        self.note = ttk.Label(
            self.root, text="Quick Note",
            font=Bases.label, anchor="center"
        )
        self.vendor = ttk.Label(
            self.root, text="Vendor",
            font=Bases.label, anchor="center"
        )
        self.gal_lb = ttk.Label(
            self.root, text="Lbs. Per Gal",
            font=Bases.label, anchor="center"
        )
        self.low_inventory = ttk.Label(
            self.root,
            text="Low Inventory Level",
            font=Bases.label,
            anchor="center",
        )
        self.system = ttk.Label(
            self.root, text="Ink System",
            font=Bases.label, anchor="center"
        )
        self.search = ttk.Label(
            self.root, text="Search", font=Bases.label, anchor="center"
        )
        self.health = ttk.Label(
            self.root, text="Health", font=Bases.button, anchor="e"
        )
        self.flammability = ttk.Label(
            self.root, text="Flammability", font=Bases.button, anchor="e"
        )
        self.reactivity = ttk.Label(
            self.root, text="Reactivity", font=Bases.button, anchor="e"
        )
        self.ppe = ttk.Label(
            self.root, text="PPE", font=Bases.button, anchor="e"
        )
        self.revision = ttk.Label(
            self.root, text="Revision", font=Bases.button, anchor="e"
        )
        self.revision_version = ttk.Label(
            self.root, text="00", font=Bases.button, anchor="w"
        )
        self.index = ttk.Label(
            self.root, text='', font=Bases.button, anchor='center'
        )
    
    def create_entries(self):
        """Create entry widgets"""
        self.base_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.alt_name_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.description_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.cost_entry = ttk.Entry(
            self.root,font=Bases.data, state="disabled"
        )
        self.note_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.vendor_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.gal_lb_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.low_inventory_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.system_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.search_entry = ttk.Entry(
            self.root, font=Bases.data, state="normal"
        )
        self.health_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.flammability_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.reactivity_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )
        self.ppe_entry = ttk.Entry(
            self.root, font=Bases.data, state="disabled"
        )

    def create_buttons(self):
        """Create button widgets"""
        self.edit_btn = ttk.Button(
            self.root, text="Edit Base",
           command=lambda: self.edit_bases()
        )
        self.delete_btn = ttk.Button(
            self.root, text="Delete Base",
            command=lambda: self.delete_handler()
        )
        self.new_btn = ttk.Button(
            self.root, text="New Base", command=lambda: self.new_record()
        )
        self.report_btn = ttk.Button(
            self.root, text="Useage Report",
        )
        self.usage_btn = ttk.Button(
            self.root, text="Calculate Usage",
        )
        self.rename_btn = ttk.Button(
            self.root, text="Rename Base",
        )
        self.print_btn = ttk.Button(
            self.root, text="Print Base",
        )
        self.save_btn = ttk.Button(
            self.root, text="Save Base",
            state='disabled',
            command=lambda: self.save()
        )
        self.first_record_btn = ttk.Button(
            self.root, text="<<",
            command=lambda: self.first_record()
        )
        self.previous_record_btn = ttk.Button(
            self.root, text="<",
            command=lambda: self.previous_record()
        )
        self.next_record_btn = ttk.Button(
            self.root, text=">",
            command=lambda: self.next_record()
        )
        self.last_record_btn = ttk.Button(
            self.root, text=">>",
            command=lambda: self.last_record()
        )

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

    def user_level(self):
        '''Disable features based on the users level'''
        level = self.commands.user_assignments()
        if level <= 2:
            self.edit_btn.config(state='disabled')
            self.new_btn.config(state='disabled')
            self.delete_btn.config(state='disabled')
            self.rename_btn.config(state='disabled')
        if level == 1:
            self.usage_btn.config(state='disabled')

    def edit_bases(self):
        '''Functionality for edit button'''
        self.commands.connect()
        if self.edit_btn.cget('text') == 'Edit Base':
            self.state = 'Edit'
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
            self.state = None
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
            self.commands.disconnect()
            self.populate_base()

    def create_table(self):
        # Create voc table
        self.table = ttk.Treeview(self.root)
        self.table['columns'] = ('Name', 'Amount')
        # Format columns
        self.table.column('#0', width=50, minwidth=50)
        self.table.column('Name', width=125, minwidth=125)
        self.table.column('Amount', width=225, minwidth=225)
        # Create headings
        self.table.heading('#0', text='ID', anchor='w')
        self.table.heading('Name', text='Name', anchor='w')
        self.table.heading('Amount', text='Amount', anchor='w')
        self.table.place(x=390, y=115, width=400, height=150)
        # Populate table
        self.populate_table()

    def populate_table(self):
        for voc in self.table.get_children():
            self.table.delete(voc)
        voc_list = self.commands.populate_voc(self.base_entry.get())
        for index, data in enumerate(voc_list):
            self.table.insert(
                parent='', index='end', iid=index+1, text=str(index+1),
                values=data
            )
    
    def populate_base(self):
        self.index.config(
            text=f'{self.current_index +1}/{self.commands.count_bases()}'
        )
        record = self.commands.get_base(self.current_index)
        # Update Name
        self.base_entry.configure(state='normal')
        self.base_entry.delete(0, 'end')
        self.base_entry.insert(0, record[0])
        self.base_entry.configure(state='disable')
        # Update alternative name
        self.alt_name_entry.configure(state='normal')
        self.alt_name_entry.delete(0, 'end')
        self.alt_name_entry.insert(0, record[1])
        self.alt_name_entry.configure(state='disable')
        # Update description
        self.description_entry.configure(state='normal')
        self.description_entry.delete(0, 'end')
        self.description_entry.insert(0, record[10])
        self.description_entry.configure(state='disable')
        # update cost
        self.cost_entry.configure(state='normal')
        self.cost_entry.delete(0, 'end')
        self.cost_entry.insert(0, record[2])
        self.cost_entry.configure(state='disable')
        # Update note
        self.cost_entry.configure(state='normal')
        self.cost_entry.delete(0, 'end')
        self.cost_entry.insert(0, record[9])
        self.cost_entry.configure(state='disable')
        # Update vendor
        self.vendor_entry.configure(state='normal')
        self.vendor_entry.delete(0, 'end')
        self.vendor_entry.insert(0, record[11])
        self.vendor_entry.configure(state='disable')
        # Update lbs
        self.gal_lb_entry.configure(state='normal')
        self.gal_lb_entry.delete(0, 'end')
        self.gal_lb_entry.insert(0, record[13])
        self.gal_lb_entry.configure(state='disable')
        # Update inventory
        self.low_inventory_entry.configure(state='normal')
        self.low_inventory_entry.delete(0, 'end')
        self.low_inventory_entry.insert(0, record[7])
        self.low_inventory_entry.configure(state='disable')
        # Update ink system
        self.system_entry.configure(state='normal')
        self.system_entry.delete(0, 'end')
        self.system_entry.insert(0, record[12])
        self.system_entry.configure(state='disable')
        # Update health
        self.health_entry.configure(state='normal')
        self.health_entry.delete(0, 'end')
        self.health_entry.insert(0, record[3])
        self.health_entry.configure(state='disable')
        # Update flammability
        self.flammability_entry.configure(state='normal')
        self.flammability_entry.delete(0, 'end')
        self.flammability_entry.insert(0, record[4])
        self.flammability_entry.configure(state='disable')
        # Update reactivity
        self.reactivity_entry.configure(state='normal')
        self.reactivity_entry.delete(0, 'end')
        self.reactivity_entry.insert(0, record[5])
        self.reactivity_entry.configure(state='disable')
        # Update PPE
        self.ppe_entry.configure(state='normal')
        self.ppe_entry.delete(0, 'end')
        self.ppe_entry.insert(0, record[6])
        self.ppe_entry.configure(state='disable')
        # Update revision
        self.revision_version.configure(text=record[8])
        self.populate_table()
    
    def on_close(self):
        '''How to handle the x button.'''
        try:
            self.commands.disconnect()
        except Exception:
            pass
        finally:
            self.menu.deiconify()
            self.root.destroy()
    
    def first_record(self):
        self.current_index = 0
        self.populate_base()
    
    def previous_record(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.populate_base()

    def next_record(self):
        if self.current_index != int(self.commands.count_bases()) - 1:
            self.current_index += 1
            self.populate_base()
    
    def last_record(self):
        self.current_index = int(self.commands.count_bases()) - 1
        self.populate_base()
    
    def delete_handler(self):
        if self.delete_btn.cget('text') == 'Delete Base':
            base = self.base_entry.get()
            messagebox.askyesnocancel(
                title='Delete Base',
                message=f'Are you sure you want to delete {base}'
            )
            #self.commands.delete_base(base)
        elif self.delete_btn.cget('text') == 'Delete VOC':
            try:
                voc = self.table.item(self.table.focus())['values'][0]
                status = self.commands.delete_voc(self.base_entry.get(), voc)
                if status:
                    voc = self.table.selection()[0]
                    self.table.delete(voc)
            except IndexError:
                messagebox.showwarning(
                    title="No VOC Selected.",
                    message='Please select a VOC to delete.'
                )
            except Exception as e:
                print(e)
    
    def save(self):
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
            if self.state == 'Edit':
                vocs = [self.table.item(x)['values'] for x in self.table.get_children()]
                self.commands.save_base(values, vocs)
                self.state = None
            elif self.state == 'New':
                pass
                #self.commands.new_base(values)
                #self.index = len(self.commands.count_bases()) - 1
                #self.state = None
            self.populate_base()
            self.edit_bases()
        except ValueError:
            messagebox.showerror(
                title='Mismatch Information.',
                message='Please ensure all information is valid.'
            )

    def new_record(self):
        if self.new_btn.cget('text') == 'New Base':
            self.state = 'New'
            self.edit_bases()
            self.base_entry.config(state='normal')
            index = int(self.commands.count_bases()) + 1
            self.index.config(text=f'*{index}/{index}*')
            self.revision_version.config(text='1')
            self.base_entry.delete(0, 'end')
            self.alt_name_entry.delete(0, 'end')
            self.description_entry.delete(0, 'end')
            self.cost_entry.delete(0, 'end')
            self.note_entry.delete(0, 'end')
            self.vendor_entry.delete(0, 'end')
            self.gal_lb_entry.delete(0, 'end')
            self.low_inventory_entry.delete(0, 'end')
            self.system_entry.delete(0, 'end')
            self.health_entry.delete(0, 'end')
            self.flammability_entry.delete(0, 'end')
            self.reactivity_entry.delete(0, 'end')
            self.ppe_entry.delete(0, 'end')
            for voc in self.table.get_children():
                self.table.delete(voc)
        elif self.new_btn.cget('text') == 'Add VOC':
            index = len(self.table.get_children()) + 1
            voc_list = [x[0] for x in self.commands.voc_list()]
            voc = Voc(index, voc_list, self.add_voc)
    
    def add_voc(self, voc, percent, index):
        self.table.insert(
            parent='', index='end', iid=index, text=str(index),
            values=(voc, percent)
        )
        self.new_btn.config(state='normal')
        print(voc, percent, index)

    def print_vocs(self, event):
        for voc in self.table.get_children():
            print(self.table.item(voc)['values'])
        print("Vocs")
        voc_list = [self.table.item(x)['values'] for x in self.table.get_children()]
        print(voc_list)


class Voc:
    label = ('Arial', 12)

    def __init__(self, index, voc_list, add_voc):
        self.window = tk.Toplevel()
        self.index = index
        self.width = 300
        self.height = 100
        swidth = self.window.winfo_screenwidth()
        sheight = self.window.winfo_screenheight()
        x = int(swidth/2 - self.width/2)
        y = int(sheight/2 - self.height/2)
        self.window.title('Add VOC')
        self.window.geometry(f'{self.width}x{self.height}+{x}+{y}')
        self.window.protocol('WM_DELETE_WINDOW', self.on_close)
        self.add_voc = add_voc
        # Labels
        self.voc = ttk.Label(self.window, text='Select VOC', font=Voc.label)
        self.amount = ttk.Label(self.window, text='Amount', font=Voc.label)
        # Create drop down
        self.voc_var = tk.StringVar()
        self.voc_list = voc_list
        self.voc_value = ttk.Combobox(
            self.window, textvariable=self.voc_var
        )
        self.voc_value['values'] = self.voc_list
        self.voc_value['state'] = 'readonly'
        self.amount_entry = ttk.Entry(self.window, font=Voc.label)
        self.submit_btn = ttk.Button(
            self.window, text='Add Voc', command=lambda: self.submit()
        )
        self.window.option_add('*TCombobox*Listbox.font', Voc.label)
        self.voc.grid(row=0, column=0)
        self.voc_value.grid(row=0, column=1)
        self.amount.grid(row=1, column=0)
        self.amount_entry.grid(row=1, column=1)
        self.submit_btn.grid(row=2, column=0)


    def submit(self):
        try:
            if (self.voc_var.get() != '' and
                self.amount_entry.get() != '' and
                float(self.amount_entry.get()) > 0):
                self.add_voc(self.voc_var.get(), self.amount_entry.get(), self.index)
                self.index += 1
            else:
                messagebox.showinfo(
                    title='Missing Information',
                    message='Please ensure both fields are populated and amount is a number.'
                )
        except Exception as e:
            messagebox.showerror(
                title='Error Adding Voc',
                message=e
            )
        
    def on_close(self):
        self.window.destroy()

        