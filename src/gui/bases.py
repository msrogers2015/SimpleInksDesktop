import tkinter as tk

class Bases:
    title = ("Comic Sans MS", 24)
    label = ("Comic Sans MS", 18)
    button = ("Comic Sans MS", 14)

    def __init__(self, logged_user, menu):
        '''Initialize base window'''
        self.logged_user = logged_user
        self.width = 800
        self.height = 600
        self.menu = menu
        # Hide menu window
        self.menu.withdraw()
        self.create_widgets()

    def create_widgets(self):
        self.base_root = tk.Tk()
        self.base_root.title('SimpleInks MS - Bases')
        self.x = int(self.base_root.winfo_screenwidth()/2 - self.width/2)
        self.y = int(self.base_root.winfo_screenheight()/2 - self.height/2)
        self.base_root.geometry(f'{self.width}x{self.height}+{self.x}+{self.y}')
        self.title = tk.Label(
            self.base_root, text='Base Materials', font=Bases.title
        )
        self.place_widgets()

    def place_widgets(self):
        self.title.place(x=200,y=5,width=400,height=35)
        self.base_root.protocol('WM_DELETE_WINDOW', self.on_close)
        self.base_root.mainloop()

    def on_close(self):
        self.base_root.destroy()
        self.menu.deiconify()