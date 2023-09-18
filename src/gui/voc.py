import tkinter as tk
from tkinter import ttk, messagebox
from functions import voc_commands


class VOCs:
    title = ("Arial", 24)
    label = ("Arial", 18)
    button = ("Arial", 14)
    data = ("Arial", 12)

    def __init__(self, logged_user, menu):
        self.logged_user = logged_user
        self.width = 400
        self.height = 615
        self.menu = menu
        self.current_index = 0
        # Create connection to functions
        self.vc = voc_commands.VocCommands(logged_user=logged_user)
        self.data = self.vc.load_vocs()
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
        self.voc_root.title("SimpleInks MS - VOCs")
        self.x = int(self.voc_root.winfo_screenwidth() / 2 - self.width / 2)
        self.y = int(self.voc_root.winfo_screenheight() / 2 - self.height / 2)
        self.voc_root.geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")
        self.voc_root.protocol("WM_DELETE_WINDOW", self.on_close)

    def create_labels(self):
        self.title = ttk.Label(
            self.voc_root,
            text="VOC Materials",
            font=VOCs.title,
            anchor='center'
        )
        self.name = ttk.Label(
            self.voc_root,
            text="VOC Name",
            font=VOCs.label,
            anchor='center'
        )
        self.alt_name = ttk.Label(
            self.voc_root,
            text="Alternative Name",
            font=VOCs.label,
            anchor='center'
        )
        self.formula = ttk.Label(
            self.voc_root,
            text="Formula",
            font=VOCs.label,
            anchor='center'
        )
        self.notes = ttk.Label(
            self.voc_root,
            text="Notes",
            font=VOCs.label,
            anchor='center'
        )
        self.index = ttk.Label(
            self.voc_root, text="", font=VOCs.button, anchor='center'
        )

    def create_entries(self):
        self.name_entry = ttk.Entry(
            self.voc_root, state="disabled", font=VOCs.data)
        self.alt_name_entry = ttk.Entry(
            self.voc_root, state="disabled", font=VOCs.data)
        self.formula_entry = ttk.Entry(
            self.voc_root, state="disabled", font=VOCs.data)
        self.notes_entry = ttk.Entry(
            self.voc_root, state="disabled", font=VOCs.data)

    def create_buttons(self):
        self.new_btn = ttk.Button(
            self.voc_root,
            text="New VOC",
            command=lambda: self.new(),
        )
        self.delete_btn = ttk.Button(
            self.voc_root,
            text="Delete VOC",
            command=lambda: self.delete(),
        )
        self.edit_btn = ttk.Button(
            self.voc_root,
            text="Edit VOC",
            command=lambda: self.edit_voc(),
        )

        self.menu_btn = ttk.Button(
            self.voc_root,
            text="Menu",
            command=lambda: self.on_close(),
        )
        self.first_btn = ttk.Button(
            self.voc_root,
            text="<<",
            command=lambda: self.first_record(),
        )
        self.previous_btn = ttk.Button(
            self.voc_root,
            text="<",
            command=lambda: self.previous_record(),
        )
        self.next_btn = ttk.Button(
            self.voc_root,
            text=">",
            command=lambda: self.next_record(),
        )
        self.last_btn = ttk.Button(
            self.voc_root,
            text=">>",
            command=lambda: self.last_record(),
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
            self.edit_btn.config(state="disabled")
            self.new_btn.config(state="disabled")
            self.delete_btn.config(state="disabled")

    def populate_voc(self):
        name, alt_name, formula, notes = self.data[self.current_index]
        self.name_entry.configure(state="normal")
        self.name_entry.delete(0, "end")
        self.name_entry.insert(0, name)
        self.name_entry.configure(state="disable")

        self.alt_name_entry.configure(state="normal")
        self.alt_name_entry.delete(0, "end")
        self.alt_name_entry.insert(0, alt_name)
        self.alt_name_entry.configure(state="disable")

        self.formula_entry.configure(state="normal")
        self.formula_entry.delete(0, "end")
        self.formula_entry.insert(0, formula)
        self.formula_entry.configure(state="disable")

        self.notes_entry.configure(state="normal")
        self.notes_entry.delete(0, "end")
        self.notes_entry.insert(0, notes)
        self.notes_entry.configure(state="disable")

        self.index.config(text=f"{self.current_index+1}/{len(self.data)}")

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

    def edit_voc(self):
        if self.edit_btn.cget("text") == "Edit VOC":
            self.new_btn.config(state="disabled")
            self.menu_btn.config(state="disabled")

            self.first_btn.config(state="disabled")
            self.previous_btn.config(state="disabled")
            self.next_btn.config(state="disabled")
            self.last_btn.config(state="disabled")

            self.name_entry.config(state="normal")
            self.notes_entry.config(state="normal")
            self.formula_entry.config(state="normal")
            self.alt_name_entry.config(state="normal")

            self.edit_btn.config(text="Save")
            self.delete_btn.config(text="Cancel")
        else:
            # Save edits
            data = [
                self.alt_name_entry.get(),
                self.formula_entry.get(),
                self.notes_entry.get(),
                self.name_entry.get(),
            ]
            status = self.vc.edit_record(data)
            if not status[0]:
                self.save_failure(status[1])

            self.new_btn.config(state="normal")
            self.menu_btn.config(state="normal")

            self.first_btn.config(state="normal")
            self.previous_btn.config(state="normal")
            self.next_btn.config(state="normal")
            self.last_btn.config(state="normal")

            self.name_entry.config(state="disabled")
            self.notes_entry.config(state="disabled")
            self.formula_entry.config(state="disabled")
            self.alt_name_entry.config(state="disabled")

            self.edit_btn.config(text="Edit VOC")
            self.delete_btn.config(text="Delete VOC")
            self.data = self.vc.load_vocs()
            self.populate_voc()

    def delete(self):
        if self.delete_btn.cget("text") == "Cancel":
            self.new_btn.config(state="normal")
            self.edit_btn.config(state="normal")
            self.menu_btn.config(state="normal")

            self.first_btn.config(state="normal")
            self.previous_btn.config(state="normal")
            self.next_btn.config(state="normal")
            self.last_btn.config(state="normal")

            self.name_entry.config(state="disabled")
            self.notes_entry.config(state="disabled")
            self.formula_entry.config(state="disabled")
            self.alt_name_entry.config(state="disabled")

            self.edit_btn.config(text="Edit VOC")
            self.delete_btn.config(text="Delete VOC")
            self.new_btn.config(text="New VOC")

            self.index.config(text=f"{self.current_index+1}/{len(self.data)}")
            self.populate_voc()
        else:
            status = messagebox.askyesno(
                title="Delete Record",
                message=f"Delete {self.name_entry.get()}?",
            )
            if status:
                self.vc.delete_record(self.name_entry.get())
                self.data = self.vc.load_vocs()
                self.current_index -= 1
                self.populate_voc()

    def new(self):
        if self.new_btn.cget("text") == "New VOC":
            self.edit_btn.config(state="disabled")
            self.menu_btn.config(state="disabled")

            self.first_btn.config(state="disabled")
            self.previous_btn.config(state="disabled")
            self.next_btn.config(state="disabled")
            self.last_btn.config(state="disabled")

            self.name_entry.config(state="normal")
            self.name_entry.delete(0, "end")
            self.notes_entry.config(state="normal")
            self.notes_entry.delete(0, "end")
            self.formula_entry.config(state="normal")
            self.formula_entry.delete(0, "end")
            self.alt_name_entry.config(state="normal")
            self.alt_name_entry.delete(0, "end")

            self.new_btn.config(text="Save")
            self.delete_btn.config(text="Cancel")
            self.index.config(text=f"*{len(self.data)+1}/{len(self.data) +1}*")
        else:
            data = [
                self.name_entry.get(),
                self.alt_name_entry.get(),
                self.formula_entry.get(),
                self.notes_entry.get(),
            ]
            # Save New record
            status = self.vc.new_record(data)
            if not status[0]:
                self.save_failure(status[1])
            self.edit_btn.config(state="normal")
            self.menu_btn.config(state="normal")

            self.first_btn.config(state="normal")
            self.previous_btn.config(state="normal")
            self.next_btn.config(state="normal")
            self.last_btn.config(state="normal")

            self.name_entry.config(state="disabled")
            self.notes_entry.config(state="disabled")
            self.formula_entry.config(state="disabled")
            self.alt_name_entry.config(state="disabled")

            self.new_btn.config(text="New VOC")
            self.delete_btn.config(text="Delete VOC")
            self.data = self.vc.load_vocs()
            self.current_index = len(self.data) - 1
            self.populate_voc()

            self.index.config(text=f"{self.current_index+1}/{len(self.data)}")

    def save_failure(self, error):
        messagebox.showerror(title="Save Failure", message=error)
