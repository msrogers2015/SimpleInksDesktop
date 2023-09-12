import tkinter as tk
from os import path, getcwd
from gui import login, bases, voc


class Menu:
    title = ("Comic Sans MS", 24)
    button = ("Comic Sans MS", 14)

    def __init__(self, logged_user, window):
        """Initialize menu."""
        # Saved logged user
        self.logged_user = logged_user
        # Destroy login window
        window.destroy()
        self.width = 600
        self.height = 500

    def create_widgets(self):
        """Create menu window."""
        self.menu_root = tk.Tk()
        self.menu_root.title("SmipleInks MS - Menu")
        # Create variables for placing window and place and size window.
        self.x = int(self.menu_root.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(
            self.menu_root.winfo_screenheight() / 2 - self.height / 2
        )
        self.menu_root.geometry(
            f"{self.width}x{self.height}+{self.x}+{self.y}"
        )
        # Create widgets for menu
        self.title = tk.Label(
            self.menu_root, text="SimpleInks MS", font=Menu.title, anchor="nw"
        )
        # Create Buttons
        self.vocs = tk.Button(
            self.menu_root, text="VOCs", font=Menu.button,
            command=lambda: voc.VOCs(self.logged_user, self.menu_root)
        )
        self.bases = tk.Button(
            self.menu_root,
            text="Bases",
            font=Menu.button,
            command=lambda: bases.Bases(self.logged_user, self.menu_root),
        )
        self.formulas = tk.Button(
            self.menu_root, text="Formulas", font=Menu.button
        )
        # Row 2
        self.raw_inv = tk.Button(
            self.menu_root, text="Raw Inventory", font=Menu.button
        )
        self.rework_inv = tk.Button(
            self.menu_root, text="Rework Inventory", font=Menu.button
        )
        self.designs = tk.Button(
            self.menu_root, text="Designs", font=Menu.button
        )
        # Row 3
        self.production = tk.Button(
            self.menu_root, text="Production", font=Menu.button
        )
        self.material_reciving = tk.Button(
            self.menu_root, text="Material Reciving", font=Menu.button
        )
        self.reports = tk.Button(
            self.menu_root, text="Reports", font=Menu.button
        )

        self.settings = tk.Button(
            self.menu_root, text="Settings", font=Menu.button
        )
        self.user_info = tk.Button(
            self.menu_root, text="Users", font=Menu.button
        )
        self.log_out = tk.Button(
            self.menu_root,
            text="Logout",
            font=Menu.button,
            command=lambda: self.log_out_(),
        )
        self.place_widgets()

    def place_widgets(self):
        """Place widgets in menu window."""
        width_ = 170
        height_ = 50
        x1 = 22
        y1 = 102
        x_space = 192
        y_space = 75
        self.title.place(x=20, y=15, width=300, height=50)
        # Row 1
        self.vocs.place(
            x=x1, y=y1, width=width_, height=height_)
        self.bases.place(
            x=x1+x_space, y=y1, width=width_, height=height_)
        self.formulas.place(
            x=x1+(x_space*2), y=y1, width=width_, height=height_)
        # Row 2
        self.raw_inv.place(
            x=x1, y=y1 + y_space, width=width_, height=height_)
        self.rework_inv.place(
            x=x1 + x_space, y=y1 + y_space, width=width_, height=height_)
        self.designs.place(
            x=x1+(x_space*2), y=y1 + y_space, width=width_, height=height_)
        # Row 3
        self.production.place(
            x=x1, y=y1+(y_space*2), width=width_, height=height_)
        self.material_reciving.place(
            x=x1+x_space, y=y1+(y_space*2), width=width_, height=height_)
        self.reports.place(
            x=x1+(x_space*2), y=y1+(y_space*2), width=width_, height=height_)
        # Row 4
        self.settings.place(
            x=x1, y=y1+(y_space*3), width=width_, height=height_)
        self.user_info.place(
            x=x1+x_space, y=y1+(y_space*3), width=width_, height=height_)
        self.log_out.place(
            x=x1+(x_space*2), y=y1+(y_space*3), width=width_, height=height_)
        
        self.menu_root.mainloop()

    def log_out_(self):
        """Log out and display login window."""
        # Destroy menu window
        self.menu_root.destroy()
        # Create login window
        self.login_gui = login.Login()
        self.login_gui.create_widgets()
