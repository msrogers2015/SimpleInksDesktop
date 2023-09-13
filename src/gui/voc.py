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
        self.height = 600
        self.menu = menu
        self.current_index = 0
        # Create connection to functions
        self.vc = voc_commands.VocCommands(logged_user=logged_user)
        self.vc.connect()
        self.menu.withdraw()
        self.create_window()
        self.create_labels()
        self.create_entries()
        self.create_buttons()
        self.place_widget()
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
            self.voc_root, text='VOC Materials', font = VOCs.label
        )
        self.alt_name = tk.Label(
            self.voc_root, text='Alternative Name', font=VOCs.label
        )
        self.description = tk.Label(
            self.voc_root, text='Description', font=VOCs.label
        )
        self.notes = tk.Label(
            self.voc_root, text='Notes', font=VOCs.label
        )
    
    def create_entries(self):
        self.name_entry = tk.Entry(
            self.voc_root, state='disabled', font= VOCs.data
        )
        self.alt_name_entry = tk.Entry(
            self.voc_root, state='disabled', font= VOCs.data
        )
        self.description_entry = tk.Entry(
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
            command=lambda: self.on_close
        )
        self.first_btn = tk.Button(
            self.voc_root, text='<<', justify='center', font = VOCs.button
        )
        self.previous_btn = tk.Button(
            self.voc_root, text='<', justify='center', font = VOCs.button
        )
        self.next_btn = tk.Button(
            self.voc_root, text='>', justify='center', font = VOCs.button
        )
        self.last_btn = tk.Button(
            self.voc_root, text='>>', justify='center', font = VOCs.button
        )
    
    def place_widget(self):
        self.title.place(x=10, y=10, width=380, height=40)
        self.name.place(x=10, y=75, width=380, height=30)
        self.alt_name.place(x=10, y=145, width=380, height=30)
        self.description.place(x=10, y=215, width=380, height=30)
        self.notes.place(x=10, y=315, width=380, height=30)
        # Place entries
        self.name_entry.place(x=10, y=105, width=380, height=30)
        self.alt_name_entry.place(x=10, y=175, width=380, height=30)
        self.description_entry.place(x=10, y=245, width=380, height=60)
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