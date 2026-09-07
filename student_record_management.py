import csv
import os
import tkinter as tk
from tkinter import ttk, messagebox

TEXT_FILE = "student.txt"
CSV_FILE = "student.csv"
HEADERS = ["ID", "Name", "Age", "Course", "City"]


class StudentRecordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Record Management System")
        self.root.state("zoomed")
        self.root.minsize(900, 600)

        self.setup_style()
        self.build_ui()
        self.load_records()

    def setup_style(self):
        style = ttk.Style()
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass

        style.configure("Treeview", rowheight=32, font=("Segoe UI", 11))
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=8)

    def build_ui(self):
        title = tk.Label(
            self.root,
            text="STUDENT RECORD MANAGEMENT SYSTEM",
            font=("Segoe UI", 24, "bold"),
            pady=18
        )
        title.pack(fill="x")

        form = tk.LabelFrame(
            self.root,
            text=" Student Details ",
            font=("Segoe UI", 13, "bold"),
            padx=18,
            pady=18,
            bd=3,
            relief="groove"
        )
        form.pack(fill="x", padx=25, pady=10)

        self.entries = {}
        for i, field in enumerate(HEADERS):
            tk.Label(form, text=f"{field}:", font=("Segoe UI", 11, "bold")).grid(
                row=0, column=i, padx=8, pady=(0, 6), sticky="w"
            )
            entry = tk.Entry(form, font=("Segoe UI", 11), width=20)
            entry.grid(row=1, column=i, padx=8, pady=5, sticky="ew")
            self.entries[field] = entry

        for i in range(len(HEADERS)):
            form.grid_columnconfigure(i, weight=1)

        buttons = tk.Frame(self.root)
        buttons.pack(fill="x", padx=25, pady=8)

        commands = [
            ("Add", self.add_record),
            ("Update", self.update_record),
            ("Delete", self.delete_record),
            ("Search", self.search_record),
            ("Refresh", self.refresh_records),
            ("Clear", self.clear_fields),
        ]
        for text, command in commands:
            ttk.Button(buttons, text=text, command=command).pack(
                side="left", padx=5, pady=5
            )

        table_frame = tk.Frame(self.root)
        table_frame.pack(fill="both", expand=True, padx=25, pady=(5, 25))

        self.tree = ttk.Treeview(table_frame, columns=HEADERS, show="headings")
        for col in HEADERS:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150)

        scrollbar = ttk.Scrollbar(
            table_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        self.tree.bind("<<TreeviewSelect>>", self.select_record)

        self.status = tk.Label(
            self.root,
            text="Ready",
            anchor="w",
            padx=25,
            pady=5,
            font=("Segoe UI", 10)
        )
        self.status.pack(fill="x")

    def get_values(self):
        return [self.entries[field].get().strip() for field in HEADERS]

    def validate(self, values):
        if any(not value for value in values):
            messagebox.showwarning("Validation", "Please fill in all fields.")
            return False
        try:
            age = int(values[2])
            if age <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Validation", "Age must be a valid positive number.")
            return False
        return True

    def add_record(self):
        values = self.get_values()
        if not self.validate(values):
            return

        if any(self.tree.item(item, "values")[0] == values[0]
               for item in self.tree.get_children()):
            messagebox.showwarning("Duplicate ID", "A student with this ID already exists.")
            return

        self.tree.insert("", "end", values=values)
        self.save_files()
        self.clear_fields()
        self.set_status("Student record added and saved.")

    def update_record(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Update", "Select a record to update.")
            return

        values = self.get_values()
        if not self.validate(values):
            return

        current_item = selected[0]
        current_id = self.tree.item(current_item, "values")[0]

        for item in self.tree.get_children():
            if item != current_item and self.tree.item(item, "values")[0] == values[0]:
                messagebox.showwarning("Duplicate ID", "Another record already uses this ID.")
                return

        self.tree.item(current_item, values=values)
        self.save_files()
        self.clear_fields()
        self.set_status(f"Record {current_id} updated and saved.")

    def delete_record(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Delete", "Select a record to delete.")
            return

        if messagebox.askyesno("Delete", "Delete the selected record?"):
            for item in selected:
                self.tree.delete(item)
            self.save_files()
            self.clear_fields()
            self.set_status("Selected record deleted.")

    def search_record(self):
        query = self.entries["ID"].get().strip().lower()
        if not query:
            messagebox.showinfo("Search", "Enter a student ID in the ID field.")
            return

        found = False
        for item in self.tree.get_children():
            values = self.tree.item(item, "values")
            if query in str(values[0]).lower():
                self.tree.selection_set(item)
                self.tree.focus(item)
                self.tree.see(item)
                self.set_status(f"Record found: {values[0]}")
                found = True
                break

        if not found:
            messagebox.showinfo("Search", "No matching student record found.")

    def refresh_records(self):
        self.load_records()
        self.clear_fields()
        self.set_status("Records refreshed from saved files.")

    def clear_fields(self):
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.tree.selection_remove(self.tree.selection())

    def select_record(self, _event=None):
        selected = self.tree.selection()
        if not selected:
            return
        values = self.tree.item(selected[0], "values")
        for field, value in zip(HEADERS, values):
            self.entries[field].delete(0, tk.END)
            self.entries[field].insert(0, value)

    def save_files(self):
        try:
            records = [
                self.tree.item(item, "values")
                for item in self.tree.get_children()
            ]

            with open(TEXT_FILE, "w", encoding="utf-8") as file:
                for record in records:
                    file.write(" | ".join(map(str, record)) + "\n")

            with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(HEADERS)
                writer.writerows(records)

        except OSError as error:
            messagebox.showerror("File Error", f"Could not save records:\n{error}")

    def load_records(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        try:
            if os.path.exists(CSV_FILE):
                with open(CSV_FILE, "r", newline="", encoding="utf-8") as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        values = [row.get(header, "") for header in HEADERS]
                        if all(values):
                            self.tree.insert("", "end", values=values)
            elif os.path.exists(TEXT_FILE):
                with open(TEXT_FILE, "r", encoding="utf-8") as file:
                    for line in file:
                        values = [part.strip() for part in line.strip().split("|")]
                        if len(values) == len(HEADERS):
                            self.tree.insert("", "end", values=values)

            self.set_status("Records loaded successfully.")

        except (OSError, csv.Error) as error:
            messagebox.showerror("File Error", f"Could not load records:\n{error}")

    def set_status(self, text):
        self.status.config(text=text)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordApp(root)
    root.mainloop()
