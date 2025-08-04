import tkinter as tk
from tkinter import messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        # Variables for options
        self.length_var = tk.IntVar(value=12)
        self.include_upper = tk.BooleanVar(value=True)
        self.include_lower = tk.BooleanVar(value=True)
        self.include_digits = tk.BooleanVar(value=True)
        self.include_symbols = tk.BooleanVar(value=True)

        self.create_widgets()

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Password Generator", font=("Helvetica", 18, "bold")).pack(pady=10)

        # Length
        length_frame = tk.Frame(self.root)
        length_frame.pack(pady=5)
        tk.Label(length_frame, text="Password Length:", font=("Helvetica", 12)).pack(side=tk.LEFT)
        tk.Spinbox(length_frame, from_=4, to=32, textvariable=self.length_var, width=5, font=("Helvetica", 12)).pack(side=tk.LEFT)

        # Options
        options_frame = tk.Frame(self.root)
        options_frame.pack(pady=5)

        tk.Checkbutton(options_frame, text="Include Uppercase", variable=self.include_upper, font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Lowercase", variable=self.include_lower, font=("Helvetica", 12)).grid(row=1, column=0, sticky="w")
        tk.Checkbutton(options_frame, text="Include Digits", variable=self.include_digits, font=("Helvetica", 12)).grid(row=0, column=1, sticky="w")
        tk.Checkbutton(options_frame, text="Include Symbols", variable=self.include_symbols, font=("Helvetica", 12)).grid(row=1, column=1, sticky="w")

        # Generate Button
        tk.Button(self.root, text="Generate Password", font=("Helvetica", 14), command=self.generate_password).pack(pady=10)

        # Output Entry
        self.password_entry = tk.Entry(self.root, font=("Helvetica", 14), width=28, justify='center')
        self.password_entry.pack(pady=5)

        # Copy Button
        tk.Button(self.root, text="Copy to Clipboard", font=("Helvetica", 12), command=self.copy_password).pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()

        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4")
            return

        char_set = ""
        if self.include_upper.get():
            char_set += string.ascii_uppercase
        if self.include_lower.get():
            char_set += string.ascii_lowercase
        if self.include_digits.get():
            char_set += string.digits
        if self.include_symbols.get():
            char_set += string.punctuation

        if not char_set:
            messagebox.showwarning("Warning", "Select at least one character type!")
            return

        password = ''.join(random.choice(char_set) for _ in range(length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def copy_password(self):
        password = self.password_entry.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
