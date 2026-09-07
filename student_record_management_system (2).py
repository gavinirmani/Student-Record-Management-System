import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

TXT_FILE = "student.txt"
CSV_FILE = "student.csv"


class StudentRecordManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System")
        self.root.geometry("1100x650")
        self.root.configure(bg="#DDF3F5")
        self.create_widgets()
        self.load_records()

    def create_widgets(self):
        # ---------------- Main window ----------------
        self.root.geometry("1280x720")
        self.root.minsize(1000, 620)
        self.root.configure(bg="#DDF3F5")

        # ---------------- Title ----------------
        title_bar = tk.Frame(self.root, bg="#CFECEF", height=85)
        title_bar.pack(fill="x")
        title_bar.pack_propagate(False)

        title = tk.Label(
            title_bar,
            text="STUDENT RECORD MANAGEMENT SYSTEM",
            font=("Arial", 36, "bold"),
            bg="#CFECEF",
            fg="#071A2F"
        )
        title.pack(expand=True, pady=(4, 0))

        # ---------------- Form ----------------
        form = tk.Frame(
            self.root,
            bg="#F4F4F2",
            bd=2,
            relief="solid",
            height=100
        )
        form.pack(fill="x", padx=48, pady=(18, 0))
        form.pack_propagate(False)

        # Exact field arrangement inspired by the reference:
        # Row 1: Name | Reg No
        # Row 2: Course | Age | City
        tk.Label(
            form, text="Name", font=("Arial", 11, "bold"),
            bg="#F4F4F2", fg="#171717"
        ).place(x=15, y=15)

        self.entries = {}

        self.entries["Name"] = tk.Entry(
            form, font=("Arial", 11), width=25, bd=1, relief="sunken"
        )
        self.entries["Name"].place(x=95, y=12)

        tk.Label(
            form, text="Reg No", font=("Arial", 11, "bold"),
            bg="#F4F4F2", fg="#171717"
        ).place(x=355, y=15)

        self.entries["Reg No"] = tk.Entry(
            form, font=("Arial", 11), width=25, bd=1, relief="sunken"
        )
        self.entries["Reg No"].place(x=465, y=12)

        tk.Label(
            form, text="Course", font=("Arial", 11, "bold"),
            bg="#F4F4F2", fg="#171717"
        ).place(x=15, y=55)

        self.entries["Course"] = tk.Entry(
            form, font=("Arial", 11), width=25, bd=1, relief="sunken"
        )
        self.entries["Course"].place(x=95, y=52)

        tk.Label(
            form, text="Age", font=("Arial", 11, "bold"),
            bg="#F4F4F2", fg="#171717"
        ).place(x=355, y=55)

        self.entries["Age"] = tk.Entry(
            form, font=("Arial", 11), width=14, bd=1, relief="sunken"
        )
        self.entries["Age"].place(x=465, y=52)

        tk.Label(
            form, text="City", font=("Arial", 11, "bold"),
            bg="#F4F4F2", fg="#171717"
        ).place(x=600, y=55)

        self.entries["City"] = tk.Entry(
            form, font=("Arial", 11), width=20, bd=1, relief="sunken"
        )
        self.entries["City"].place(x=690, y=52)

        # ---------------- Buttons ----------------
        button_frame = tk.Frame(self.root, bg="#DDF3F5")
        button_frame.pack(pady=(18, 20))

        buttons = [
            ("Add", "#3FA34D", "#2E7D32", self.add_record),
            ("Update", "#258DB7", "#176A8A", self.update_record),
            ("Delete", "#B52F23", "#8F241B", self.delete_record),
            ("Search", "#6D4AA0", "#53327E", self.search_record),
            ("Refresh", "#263A45", "#1B2931", self.refresh_records)
        ]

        for i, (text, color, active_color, command) in enumerate(buttons):
            tk.Button(
                button_frame,
                text=text,
                width=11,
                height=1,
                bg=color,
                fg="white",
                activebackground=active_color,
                activeforeground="white",
                font=("Arial", 10, "bold"),
                bd=1,
                relief="raised",
                cursor="hand2",
                command=command
            ).grid(row=0, column=i, padx=10)

        # ---------------- Table ----------------
        table_frame = tk.Frame(
            self.root,
            bg="#DDF3F5"
        )
        table_frame.pack(
            fill="both",
            expand=True,
            padx=48,
            pady=(0, 12)
        )

        columns = ("Name", "Reg No", "Course", "Age", "City")

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=11
        )

        for column in columns:
            self.tree.heading(
                column,
                text=column,
                anchor="center"
            )

        # Similar proportions to the reference screenshot.
        self.tree.column(
            "Name", width=185, minwidth=120, anchor="center"
        )
        self.tree.column(
            "Reg No", width=190, minwidth=130, anchor="center"
        )
        self.tree.column(
            "Course", width=235, minwidth=150, anchor="center"
        )
        self.tree.column(
            "Age", width=150, minwidth=80, anchor="center"
        )
        self.tree.column(
            "City", width=190, minwidth=100, anchor="center"
        )

        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        # Reference-photo table appearance.
        style.configure(
            "Treeview.Heading",
            background="#20262B",
            foreground="#FFFFFF",
            font=("Arial", 10, "bold"),
            relief="flat",
            padding=(4, 7)
        )
        style.map(
            "Treeview.Heading",
            background=[("active", "#20262B")]
        )

        style.configure(
            "Treeview",
            background="#F7F7F5",
            foreground="#303030",
            fieldbackground="#F7F7F5",
            font=("Arial", 9),
            rowheight=24,
            borderwidth=1,
            relief="solid"
        )
        style.map(
            "Treeview",
            background=[("selected", "#B7DDE5")],
            foreground=[("selected", "#071A2F")]
        )

        self.tree.tag_configure(
            "oddrow",
            background="#F7F7F5"
        )
        self.tree.tag_configure(
            "evenrow",
            background="#EEEEEC"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )
        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )
        scrollbar.pack(
            side="right",
            fill="y"
        )

        self.tree.bind(
            "<<TreeviewSelect>>",
            self.select_record
        )

        # ---------------- Footer ----------------
        footer = tk.Frame(
            self.root,
            bg="#CFECEF",
            height=34
        )
        footer.pack(fill="x", side="bottom")
        footer.pack_propagate(False)

        tk.Label(
            footer,
            text="Project by K.G.G. Nirmani | CIT-25-02-0297",
            font=("Arial", 9),
            bg="#CFECEF",
            fg="#3E5968"
        ).pack(expand=True)

    def get_values(self):
        return tuple(self.entries[x].get().strip()
                     for x in ("Name", "Reg No", "Course", "Age", "City"))

    def validate(self):
        values = self.get_values()

        if not all(values):
            messagebox.showwarning(
                "Validation Error",
                "Please fill in all fields."
            )
            return False

        try:
            if int(values[3]) <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Validation Error",
                "Age must be a valid positive number."
            )
            return False

        return True

    def add_record(self):
        if not self.validate():
            return

        values = self.get_values()

        for item in self.tree.get_children():
            if self.tree.item(item, "values")[1] == values[1]:
                messagebox.showwarning(
                    "Duplicate Record",
                    "This Registration Number already exists."
                )
                return

        self.tree.insert("", "end", values=values, tags=("evenrow" if len(self.tree.get_children()) % 2 == 0 else "oddrow",))
        self.save_records()
        self.clear_fields()

        messagebox.showinfo(
            "Success",
            "Student record added successfully."
        )

    def update_record(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Update",
                "Please select a record to update."
            )
            return

        if not self.validate():
            return

        values = self.get_values()
        selected_item = selected[0]

        for item in self.tree.get_children():
            if item != selected_item:
                if self.tree.item(item, "values")[1] == values[1]:
                    messagebox.showwarning(
                        "Duplicate Record",
                        "This Registration Number already exists."
                    )
                    return

        self.tree.item(selected_item, values=values)
        self.save_records()
        self.clear_fields()

        messagebox.showinfo(
            "Success",
            "Student record updated successfully."
        )

    def delete_record(self):
        selected = self.tree.selection()

        if not selected:
            messagebox.showwarning(
                "Delete",
                "Please select a record to delete."
            )
            return

        if messagebox.askyesno(
            "Confirm Delete",
            "Are you sure you want to delete the selected record?"
        ):
            for item in selected:
                self.tree.delete(item)

            self.save_records()
            self.clear_fields()

            messagebox.showinfo(
                "Success",
                "Student record deleted successfully."
            )

    def search_record(self):
        reg_no = self.entries["Reg No"].get().strip()

        if not reg_no:
            messagebox.showwarning(
                "Search",
                "Enter a Registration Number."
            )
            return

        for item in self.tree.get_children():
            values = self.tree.item(item, "values")

            if values[1].lower() == reg_no.lower():
                self.tree.selection_set(item)
                self.tree.focus(item)
                self.tree.see(item)
                messagebox.showinfo(
                    "Search Result",
                    "Student record found."
                )
                return

        messagebox.showinfo(
            "Search Result",
            "No record found."
        )

    def refresh_records(self):
        self.load_records()
        self.clear_fields()

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)

        for item in self.tree.selection():
            self.tree.selection_remove(item)

    def select_record(self, event=None):
        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(selected[0], "values")

        for field, value in zip(
            ("Name", "Reg No", "Course", "Age", "City"),
            values
        ):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, value)

    def save_records(self):
        try:
            records = [
                self.tree.item(item, "values")
                for item in self.tree.get_children()
            ]

            with open(TXT_FILE, "w", encoding="utf-8") as file:
                for record in records:
                    file.write(" | ".join(record) + "\n")

            with open(
                CSV_FILE, "w", newline="", encoding="utf-8"
            ) as file:
                writer = csv.writer(file)
                writer.writerow(
                    ["Name", "Reg No", "Course", "Age", "City"]
                )
                writer.writerows(records)

        except OSError as error:
            messagebox.showerror(
                "File Error",
                f"Unable to save records.\n\n{error}"
            )

    def load_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            if os.path.exists(CSV_FILE):
                with open(
                    CSV_FILE, "r",
                    newline="", encoding="utf-8"
                ) as file:
                    reader = csv.reader(file)
                    rows = list(reader)

                if rows and rows[0] == [
                    "Name", "Reg No", "Course", "Age", "City"
                ]:
                    rows = rows[1:]

                for row in rows:
                    if len(row) == 5:
                        self.tree.insert("", "end", values=row, tags=("evenrow" if len(self.tree.get_children()) % 2 == 0 else "oddrow",))

            elif os.path.exists(TXT_FILE):
                with open(TXT_FILE, "r", encoding="utf-8") as file:
                    for line in file:
                        row = [
                            x.strip()
                            for x in line.strip().split("|")
                        ]
                        if len(row) == 5:
                            self.tree.insert("", "end", values=row, tags=("evenrow" if len(self.tree.get_children()) % 2 == 0 else "oddrow",))

        except (OSError, csv.Error) as error:
            messagebox.showerror(
                "File Error",
                f"Unable to load records.\n\n{error}"
            )


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordManagementSystem(root)
    root.mainloop()
