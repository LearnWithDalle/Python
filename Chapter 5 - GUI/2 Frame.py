import tkinter as tk


class dalle(tk.Frame):
    def __init__(self, ok=None):
        super().__init__(ok)
        self.ok = ok
        self.pack()
        self.secondWidget()
    def secondWidget(self):
        self.hiThere = tk.Button(self)
        self.hiThere["text"] = "Hello dalle Bhaiya"
        self.hiThere["command"] = self.bhai
        self.hiThere.pack(side="top")
        self.quit = tk.Button(self, text="Exit Karo",fg="green", command=self.ok.destroy).pack(side="bottom")
    def bhai(self):
        print("main Print ho raha huu")
        
box = tk.Tk()
pappu = dalle(ok=box)
pappu.mainloop()