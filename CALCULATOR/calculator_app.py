import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry field
        input_frame = tk.Frame(self.root, width=400, height=50, bd=0)
        input_frame.pack(side="top")

        input_field = tk.Entry(input_frame, font=('Arial', 20), textvariable=self.input_text,
                               width=50, bg="#eee", bd=0, justify="right")
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        # Buttons
        btns_frame = tk.Frame(self.root, bg="grey")
        btns_frame.pack()

        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '^', '='],
            ['sqrt', 'log', 'sin', 'cos'],
            ['tan', 'pi', '!', 'DEL']
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button in enumerate(row):
                tk.Button(btns_frame, text=button, width=8, height=2, font=('Arial', 14),
                          fg="black", bg="#fff", bd=1, command=lambda x=button: self.click(x)).grid(row=row_index, column=col_index, padx=1, pady=1)

    def click(self, item):
        if item == 'C':
            self.expression = ""
        elif item == '=':
            self.calculate()
        elif item == 'DEL':
            self.expression = self.expression[:-1]
        elif item == 'sqrt':
            self.expression += "math.sqrt("
        elif item == 'log':
            self.expression += "math.log10("
        elif item == 'sin':
            self.expression += "math.sin(math.radians("
        elif item == 'cos':
            self.expression += "math.cos(math.radians("
        elif item == 'tan':
            self.expression += "math.tan(math.radians("
        elif item == 'pi':
            self.expression += str(math.pi)
        elif item == '!':
            self.expression += "math.factorial("
        elif item == '^':
            self.expression += "**"
        else:
            self.expression += str(item)

        self.input_text.set(self.expression)

    def calculate(self):
        try:
            result = eval(self.expression)
            self.input_text.set(result)
            self.expression = str(result)
        except Exception:
            self.input_text.set("Error")
            self.expression = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
