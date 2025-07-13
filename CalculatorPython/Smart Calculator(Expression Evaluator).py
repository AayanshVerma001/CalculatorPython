import tkinter as tk

def click(btn_text):
    if btn_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif btn_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, btn_text)

root = tk.Tk()
root.title("Advanced Calculator")

entry = tk.Entry(root, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['(', ')', '', '%']
]

for i in range(len(buttons)):
    for j in range(len(buttons[i])):
        b = tk.Button(root, text=buttons[i][j], width=5, height=2,
                      font=("Arial", 16),
                      command=lambda text=buttons[i][j]: click(text))
        b.grid(row=i+1, column=j, padx=5, pady=5)

root.mainloop()