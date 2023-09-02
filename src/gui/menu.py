import tkinter as tk
from os import path, getcwd

class Menu:
    title = ("Comic Sans MS", 24)
    button = ("Comic Sans MS", 16)
    def __init__(self, logged_user, login_window):
        self.logged_user = logged_user
        login_window.destroy()
        self.width = 400
        self.height = 600

    def create_widgets(self):
        self.root = tk.Tk()
        self.root.title('SmipleInks MS - Menu')
        self.middle_width = int(self.root.winfo_screenwidth()/2 - self.width/2)
        self.middle_height = int(self.root.winfo_screenheight()/2 - self.height/2)
        self.root.geometry(f'{self.width}x{self.height}+{self.middle_width}+{self.middle_height}')
        self.title = tk.Label(text='SimpleInks MS', font=Menu.title, anchor='nw')
        self.bases = tk.Button(text='Bases', font=Menu.button)
        self.formulas = tk.Button(text='Formulas', font=Menu.button)
        self.raw_inv = tk.Button(text='Raw Inventory', font=Menu.button)
        self.cut_inv = tk.Button(text='Cut Inventory', font=Menu.button)
        self.designs = tk.Button(text='Designs', font=Menu.button)
        self.production = tk.Button(text='Production', font=Menu.button)
        self.vocs = tk.Button(text='VOCs', font=Menu.button)
        self.reports = tk.Button(text='Reports', font=Menu.button)
        self.settings = tk.Button(text='Settings', font=Menu.button)
        self.user_info = tk.Button(text='User Info', font=Menu.button)
        self.log_out = tk.Button(text='Logout', font=Menu.button)
        self.place_widgets()

    def place_widgets(self):
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
        self.root.mainloop()

if __name__ == '__main__':
    app = Menu('admin', 'test')
    app.create_widgets()