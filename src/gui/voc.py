import tkinter as tk
from tkinter import ttk, messagebox
from functions import voc_commands


class VOCs:
    title = ("Comic Sans MS", 24)
    label = ("Comic Sans MS", 18)
    button = ("Comic Sans MS", 14)
    data = ("Comic Sans MS", 12)

    def __init__(self, logged_user, menu):
        self.logged_user = logged_user
        self.width = 400
        self.height = 615
        self.menu = menu
        self.current_index = 0
        # Create connection to functions
        self.vc = voc_commands.VocCommands(logged_user=logged_user)
        self.data = self.vc.load_bases()
        self.menu.withdraw()
        self.create_window()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.place_widget()
        self.user_level()
        self.populate_voc()
        self.voc_root.mainloop()

    def create_window(self):
        self.voc_root = tk.Tk()
        self.voc_root.title('SimpleInks MS - VOCs')
        self.x = int(self.voc_root.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.voc_root.winfo_screenheight() / 2 - self.height / 2)
        self.voc_root.geometry(
            f'{self.width}x{self.height}+{self.x}+{self.y}'
        )
        self.voc_root.protocol('WM_DELETE_WINDOW', self.on_close)

    def create_labels(self):
        self.title = tk.Label(
            self.voc_root, text='VOC Materials', font = VOCs.title
        )
        self.name = tk.Label(
            self.voc_root, text='VOC Name', font = VOCs.label
        )
        self.alt_name = tk.Label(
            self.voc_root, text='Alternative Name', font=VOCs.label
        )
        self.formula = tk.Label(
            self.voc_root, text='Formula', font=VOCs.label
        )
        self.notes = tk.Label(
            self.voc_root, text='Notes', font=VOCs.label
        )
        self.index = tk.Label(
            self.voc_root, text='', font=VOCs.button, justify='center'
        )
    
    def create_entries(self):
        self.name_entry = tk.Entry(
            self.voc_root, state='disabled', font= VOCs.data
        )
        self.alt_name_entry = tk.Entry(
            self.voc_root, state='disabled', font= VOCs.data
        )
        self.formula_entry = tk.Entry(
            self.voc_root, state='disabled', font= VOCs.data
        )
        self.notes_entry = tk.Entry(
            self.voc_root, state='disabled', font= VOCs.data
        )
        
    def create_buttons(self):
        self.new_btn = tk.Button(
            self.voc_root, text='New VOC', justify='center', font = VOCs.button
        )
        self.delete_btn = tk.Button(
            self.voc_root, text='Delete VOC', justify='center', font = VOCs.button
        )
        self.edit_btn = tk.Button(
            self.voc_root, text='Edit VOC', justify='center', font=VOCs.button
        )

        self.menu_btn = tk.Button(
            self.voc_root, text='Menu', justify='center', font=VOCs.button,
            command=lambda: self.on_close()
        )
        self.first_btn = tk.Button(
            self.voc_root, text='<<', justify='center', font = VOCs.button,
            command=lambda: self.first_record()
        )
        self.previous_btn = tk.Button(
            self.voc_root, text='<', justify='center', font = VOCs.button,
            command=lambda: self.previous_record()
        )
        self.next_btn = tk.Button(
            self.voc_root, text='>', justify='center', font = VOCs.button,
            command = lambda:self.next_record()
        )
        self.last_btn = tk.Button(
            self.voc_root, text='>>', justify='center', font = VOCs.button,
            command=lambda: self.last_record()
        )
    
    def place_widget(self):
        self.title.place(x=10, y=10, width=380, height=40)
        self.name.place(x=10, y=75, width=380, height=30)
        self.alt_name.place(x=10, y=145, width=380, height=30)
        self.formula.place(x=10, y=215, width=380, height=30)
        self.notes.place(x=10, y=315, width=380, height=30)
        self.index.place(x=140, y=580, width=120, height=35)
        # Place entries
        self.name_entry.place(x=10, y=105, width=380, height=30)
        self.alt_name_entry.place(x=10, y=175, width=380, height=30)
        self.formula_entry.place(x=10, y=245, width=380, height=60)
        self.notes_entry.place(x=10, y=345, width=380, height=60)
        # Place buttons
        self.new_btn.place(x=40, y=425, width=150, height=40)
        self.delete_btn.place(x=210, y=425, width=150, height=40)
        self.edit_btn.place(x=40, y=475, width=150, height=40)
        self.menu_btn.place(x=210, y=475, width=150, height=40)
        self.first_btn.place(x=40, y=525, width=70, height=40)
        self.previous_btn.place(x=123, y=525, width=70, height=40)
        self.next_btn.place(x=207, y=525, width=70, height=40)
        self.last_btn.place(x=290, y=525, width=70, height=40)

    def on_close(self):
        self.vc.disconnect()
        self.voc_root.destroy()
        self.menu.deiconify()

    def user_level(self):
        level = self.vc.user_assignments()
        if level <= 2:
            self.edit_btn.config(state='disabled')
            self.new_btn.config(state='disabled')
            self.delete_btn.config(state='disabled')

    def populate_voc(self):
        name, alt_name, formula, notes = self.data[self.current_index]
        self.name_entry.configure(state='normal')
        self.name_entry.delete(0, 'end')
        self.name_entry.insert(0, name)
        self.name_entry.configure(state='disable')

        self.alt_name_entry.configure(state='normal')
        self.alt_name_entry.delete(0, 'end')
        self.alt_name_entry.insert(0, alt_name)
        self.alt_name_entry.configure(state='disable')

        self.formula_entry.configure(state='normal')
        self.formula_entry.delete(0, 'end')
        self.formula_entry.insert(0, formula)
        self.formula_entry.configure(state='disable')

        self.notes_entry.configure(state='normal')
        self.notes_entry.delete(0, 'end')
        self.notes_entry.insert(0, notes)
        self.notes_entry.configure(state='disable')

        self.index.config(text=f'{self.current_index+1}/{len(self.data)}')

    def first_record(self):
        self.current_index = 0
        self.populate_voc()

    def previous_record(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.populate_voc()

    def next_record(self):
        if self.current_index != len(self.data) - 1:
            self.current_index += 1
            self.populate_voc()

    def last_record(self):
        self.current_index = len(self.data) - 1
        self.populate_voc()