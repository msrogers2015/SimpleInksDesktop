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
        self.width = 800
        self.height = 600
        self.menu = menu
        self.current_index = 0
        # Create connection to functions
        self.vc = voc_commands.VocCommands(logged_user=logged_user)
        self.vc.connect()
        self.menu.withdraw()
        self.create_window()
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

    def on_close(self):
        self.vc.disconnect()
        self.voc_root.destroy()
        self.menu.deiconify()