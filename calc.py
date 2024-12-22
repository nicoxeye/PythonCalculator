import tkinter as tk


def button_click(label):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + label) 


def clear_display():
    entry.delete(0, tk.END)


def evaluate_expression():
    expression = entry.get().replace('×', '*').replace('÷', '/')
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


window = tk.Tk()
window.title("EasyCalculator")
window.config(bg="lightblue")


entry = tk.Entry(window, width=30, font=("Arial", 16), justify="right", bg="white")
entry.pack()
entry.grid(row=0, column=0, columnspan=3, sticky="nsew")


for i in range(5):
    window.grid_rowconfigure(i, weight=1)
for j in range(4):
    window.grid_columnconfigure(j, weight=1)


buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "−"],
    ["C", "0", "=", "+"],
]


for row_index, row in enumerate(buttons, start=1):
    for col_index, label in enumerate(row):
        if label in ["C", "="]:
            command = clear_display if label == "C" else evaluate_expression
            button = tk.Button(window, text=label, font=("Arial", 18), command=command, bg="white")
        else:
            button = tk.Button(window, text=label, font=("Arial", 18), command=lambda label=label: button_click(label), bg="white")
        button.grid(row=row_index, column=col_index, sticky="nsew", padx=5, pady=5)


window.mainloop()
