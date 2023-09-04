import tkinter as tk
from os import path, getcwd
from gui import login, bases

class Menu:
    title = ("Comic Sans MS", 24)
    button = ("Comic Sans MS", 16)
    
    def __init__(self, logged_user, window):
        '''Initialize menu.'''
        # Saved logged user
        self.logged_user = logged_user
        # Destroy login window
        window.destroy()
        self.width = 400
        self.height = 600

    def create_widgets(self):
        '''Create menu window.'''
        self.menu_root = tk.Tk()
        self.menu_root.title('SmipleInks MS - Menu')
        # Create variables for placing window and place and size window.
        self.x = int(self.menu_root.winfo_screenwidth()/2 - self.width/2)
        self.y = int(self.menu_root.winfo_screenheight()/2 - self.height/2)
        self.menu_root.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        # Create widgets for menu
        self.title = tk.Label(
            self.menu_root, text='SimpleInks MS', font=Menu.title, anchor='nw'
        )
        self.bases = tk.Button(
            self.menu_root, text='Bases', font=Menu.button,
            command= lambda: self.base_menu()
        )
        self.formulas = tk.Button(
            self.menu_root, text='Formulas', font=Menu.button
        )
        self.raw_inv = tk.Button(
            self.menu_root, text='Raw Inventory', font=Menu.button
        )
        self.cut_inv = tk.Button(
            self.menu_root, text='Cut Inventory', font=Menu.button
        )
        self.designs = tk.Button(
            self.menu_root, text='Designs', font=Menu.button
        )
        self.production = tk.Button(
            self.menu_root, text='Production', font=Menu.button
        )
        self.vocs = tk.Button(
            self.menu_root, text='VOCs', font=Menu.button
        )
        self.reports = tk.Button(
            self.menu_root, text='Reports', font=Menu.button
        )
        self.settings = tk.Button(
            self.menu_root, text='Settings', font=Menu.button
        )
        self.user_info = tk.Button(
            self.menu_root, text='User Info', font=Menu.button
        )
        self.log_out = tk.Button(
            self.menu_root, text='Logout', font=Menu.button,
            command=lambda: self.log_out_()
        )
        self.place_widgets()

    def place_widgets(self):
        '''Place widgets in menu window.'''
        self.title.place(x=20, y=15, width=300, height=50)
        self.bases.place(x=25,y=102,width= 163, height=50)
        self.formulas.place(x=213,y=102,width= 162, height=50)
        self.raw_inv.place(x=25,y=173,width= 163, height=50)
        self.designs.place(x=213,y=173,width= 162, height=50)
        self.cut_inv.place(x=25,y=248,width= 163, height=50)
        self.production.place(x=213,y=248,width= 162, height=50)
        self.vocs.place(x=25,y=323,width= 163, height=50)
        self.reports.place(x=213,y=323,width= 162, height=50)
        self.settings.place(x=25,y=398,width= 163, height=50)
        self.user_info.place(x=213,y=398,width= 162, height=50)
        self.log_out.place(x=25,y=473,width= 163, height=50)
        self.menu_root.mainloop()

    def log_out_(self):
        '''Log out and display login window.'''
        # Destroy menu window
        self.menu_root.destroy()
        # Create login window
        self.login_gui = login.Login()
        self.login_gui.create_widgets()
    
    def base_menu(self):
        '''Create and display base window'''
        self.base_ = bases.Bases(self.logged_user, self.menu_root)
