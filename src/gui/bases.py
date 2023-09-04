import tkinter as tk


class Bases:
    title = ("Comic Sans MS", 24)
    label = ("Comic Sans MS", 18)
    button = ("Comic Sans MS", 14)

    def __init__(self, logged_user, menu):
        """Initialize base window"""
        self.logged_user = logged_user
        self.width = 800
        self.height = 600
        self.menu = menu
        # Hide menu window
        self.menu.withdraw()
        self.create_window()
        self.create_labels()
        self.create_entries()
        self.create_buttons()

        self.place_widgets()
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

    def create_entries(self):
        """Create entry widgets"""
        self.base_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.alt_name_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.description_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.cost_entry = tk.Entry(self.base_root,
                                   font=Bases.button, state="disabled"
                                   )
        self.note_entry = tk.Entry(self.base_root,
                                   font=Bases.button, state="disabled"
                                   )
        self.vendor_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.gal_lb_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.low_inventory_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.system_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.search_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.health_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.flammability_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.reactivity_entry = tk.Entry(
            self.base_root, font=Bases.button, state="disabled"
        )
        self.ppe_entry = tk.Entry(self.base_root,
                                  font=Bases.button, state="disabled"
                                  )

    def create_buttons(self):
        """Create button widgets"""
        self.edit_btn = tk.Button(
            self.base_root, text="Edit Base", justify="center",
            font=Bases.button
        )
        self.delete_btn = tk.Button(
            self.base_root, text="Delete Base", justify="center",
            font=Bases.button
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
        self.first_record_btn = tk.Button(
            self.base_root, text="<<", justify="center", font=Bases.button
        )
        self.previous_record_btn = tk.Button(
            self.base_root, text="<", justify="center", font=Bases.button
        )
        self.next_record_btn = tk.Button(
            self.base_root, text=">", justify="center", font=Bases.button
        )
        self.last_record_btn = tk.Button(
            self.base_root, text=">>", justify="center", font=Bases.button
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
        self.first_record_btn.place(x=420, y=415, width=80, height=35)
        self.previous_record_btn.place(x=513, y=415, width=80, height=35)
        self.next_record_btn.place(x=607, y=415, width=80, height=35)
        self.last_record_btn.place(x=700, y=415, width=80, height=35)

    def on_close(self):
        self.base_root.destroy()
        self.menu.deiconify()
