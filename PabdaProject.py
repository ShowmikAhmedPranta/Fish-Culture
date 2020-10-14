import tkinter as tk
from tkinter.constants import TRUE
 
from matplotlib.pyplot import text
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


class Estimation(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.var = tk.IntVar()
        self.label = tk.Label(self, text="Enter land area in decimal=")
        self.entry = tk.Entry(self, textvariable=self.var)
        self.btn_enter = tk.Button(self, text="Enter", command=lambda:self.action_enter())
        self.btn_exit = tk.Button(self, text="Exit", command=self.destroy)
        self.label.pack()
        self.entry.pack()
        self.btn_enter.pack()
        self.btn_exit.pack()
        

    def action_enter(self):
        #print("Action Enter")
        value = self.var.get()
        #print("value",self.value)
        self.aaa=im.user_input(value)
        #print(self.aaa)
        #print(labell)
        #self.var1="Hello"
        self.estimation_text_obj = Estimation_text(self,self.aaa)
        self.estimation_text_obj.grab_set()



class Estimation_text(tk.Toplevel):
    def __init__(self,parent,aab):
        super().__init__(parent)
        self.aab = aab
        #main frame
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=tk.TRUE,padx=100,pady=50)

        #canvas
        self.first_canvas = tk.Canvas(self.main_frame)
        self.first_canvas.pack(side=tk.LEFT, fill= tk.BOTH, expand=1, padx=20, pady=10)

        #Adding a scrollbar to first_canvas
        self.first_scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=self.first_canvas.yview)
        self.first_scrollbar.pack(side=tk.RIGHT, fill= tk.Y)

        #configuring the canvas
        self.first_canvas.configure(yscrollcommand=self.first_scrollbar.set)
        self.first_canvas.bind('<Configure>', lambda e:self.first_canvas.configure(scrollregion=self.first_canvas.bbox("all")))

        #creating another frame inside the canvas
        self.second_frame = tk.Frame(self.first_canvas)

        #adding that new frame to the window
        self.first_canvas.create_window((0,0), window= self.second_frame, anchor="nw")

        self.label = tk.Label(self.second_frame, text=self.aab)

        self.label.pack(fill=tk.BOTH)



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
        self.btn2 = tk.Button(self, text="Cost, Profit calculation", command=lambda:self.open_estimation())
        self.btn3 = tk.Button(self, text="Credits", command =lambda:self.open_credit())
        self.btn4 = tk.Button(self, text="Exit", command=self.destroy)
        self.btn1.pack(padx=200, pady=25)
        self.btn2.pack(pady=25)
        self.btn3.pack(pady=25)
        self.btn4.pack(pady=25)

    def open_about(self):
        about_window = About(self)
        about_window.grab_set()


    def open_estimation(self):
        about_estimation = Estimation(self)
        about_estimation.grab_set()

    def open_credit(self):
        about_credit = Credits(self)
        about_credit.grab_set()

if(__name__=="__main__"):
    app = App()
    app.mainloop()
