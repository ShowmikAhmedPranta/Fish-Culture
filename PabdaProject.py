import tkinter as tk
import ffiisshh as im

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="""
            Pabda Fish
            --------------------------------------------------------
            Pabda Fish is a fresh water fish of Bangladesh. It is a
            common fish found in river,beel, jheel, haor, etc. It is easily
            cultivable in ponds. It has less fish-bone and is a great
            source of protein. Every age of people usually likes to eat it.
            It has a very little amount of fat.
            Pabda fish is less prone to diseases. Harvesting can be
            done usually within 3 to 6 months. It gains weight between
            30 to 50 grams within 3 to 6 months depending on cultivation.""")

        self.label.pack(padx=100, pady=50)
        self.btn = tk.Button(self,text="close", command=self.destroy)
        self.btn.pack(padx=10, pady=5)

class Credits(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="""
                Credits
                
                Showmik Ahmed Pranta
                showmikahmedpranta@gmail.com
                
                Data and literary support by
                Md. Anisur Rahman
                anisurheds@gmail.com""")
        self.label.pack(padx=100, pady= 50)
        self.btn = tk.Button(self, text="close", command= self.destroy)
        self.btn.pack(padx=10, pady=5)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.btn1 = tk.Button(self, text="about Pabda Fish", command=lambda:self.open_about())
        self.btn2 = tk.Button(self, text="Cost, Profit calculation", command=lambda:im.user_input())
        self.btn3 = tk.Button(self, text="Credits", command =lambda:self.open_credit())
        self.btn1.pack()
        self.btn2.pack()
        self.btn3.pack()

    def open_about(self):
        about_window = About(self)
        about_window.grab_set()

    def open_credit(self):
        about_credit = Credits(self)
        about_credit.grab_set()

if(__name__=="__main__"):
    app = App()
    app.mainloop()



