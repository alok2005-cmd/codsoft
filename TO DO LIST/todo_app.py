import tkinter as tk
from tkinter import messagebox, filedialog
import os

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        self.root.resizable(False, False)

        self.tasks = []

        # Title Label
        tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Task Entry
        self.task_entry = tk.Entry(root, width=30, font=("Helvetica", 12))
        self.task_entry.pack(pady=5)

        # Add Button
        tk.Button(root, text="Add Task", width=15, command=self.add_task).pack(pady=5)

        # Task List
        self.task_listbox = tk.Listbox(root, width=40, height=15, selectmode=tk.SINGLE, font=("Helvetica", 12))
        self.task_listbox.pack(pady=10)

        # Buttons Frame
        button_frame = tk.Frame(root)
        button_frame.pack(pady=5)

        tk.Button(button_frame, text="Delete Task", width=15, command=self.delete_task).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Mark as Done", width=15, command=self.mark_done).grid(row=0, column=1, padx=5)

        # Save/Load Buttons
        tk.Button(root, text="Save Tasks", width=15, command=self.save_tasks).pack(pady=3)
        tk.Button(root, text="Load Tasks", width=15, command=self.load_tasks).pack(pady=3)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task == "":
            messagebox.showwarning("Warning", "Please enter a task.")
        else:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to delete.")
        else:
            index = selected[0]
            del self.tasks[index]
            self.update_listbox()

    def mark_done(self):
        selected = self.task_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Select a task to mark as done.")
        else:
            index = selected[0]
            task = self.tasks[index]
            if not task.startswith("✔️ "):
                self.tasks[index] = f"✔️ {task}"
                self.update_listbox()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for task in self.tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Saved", "Tasks saved successfully.")

    def load_tasks(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path and os.path.exists(file_path):
            with open(file_path, "r") as f:
                self.tasks = [line.strip() for line in f]
            self.update_listbox()
            messagebox.showinfo("Loaded", "Tasks loaded successfully.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
