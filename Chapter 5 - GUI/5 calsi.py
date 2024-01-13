import tkinter as tk


def onClick(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))


def clearEntry():
    entry.delete(0, tk.END)


def calculate():
    try:
        ans = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(ans))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error Agaya")


box = tk.Tk()
box.title("Dalle Ka Calculeter")

entry = tk.Entry(box, width=20, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = ["7", "8", "9", "/",
           "4", "5", "6", "*",
           "1", "2", "3", "-",
           "0", "C", "=", "+"
           ]
rowVal = 1
colVal = 0
for button in buttons:
    tk.Button(box, text=button, padx=10, pady=10, command=lambda b=button: onClick(
        b) if b != "=" else calculate() if b == "=" else clearEntry()).grid(row=rowVal, column=colVal)
    colVal += 1
    if colVal > 3:
        colVal = 0
        rowVal += 1


box.mainloop()
