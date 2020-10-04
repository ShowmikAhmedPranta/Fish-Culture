from tkinter import *
import ffiisshh as im

root= Tk()
btn1 = Button(root,text='About Pabda Fish')
btn2 = Button(root,text='Cost, Profit Calculation')
btn4 = Button(root,text='Credits')
btn1.configure(command=lambda:print("""
Pabda Fish
--------------------------------------------------------
Pabda Fish is a fresh water fish of Bangladesh. It is a
common fish found in river,beel, jheel, haor, etc. It is easily
cultivable in ponds. It has less fish-bone and is a great
source of protein. Every age of people usually likes to eat it.
It has a very little amount of fat.
Pabda fish is less prone to diseases. Harvesting can be
done usually within 3 to 6 months. It gains weight between
30 to 50 grams within 3 to 6 months depending on cultivation.
"""))
btn2.configure(command=lambda:im.user_input())
btn4.configure(command=lambda:print("""
Credits

Showmik Ahmed Pranta
showmikahmedpranta@gmail.com

Data and literary support by
Md. Anisur Rahman
anisurheds@gmail.com"""))
#btn.config(command=lambda:print("Hello, Tkinter!"))
btn1.pack(padx=120, pady=30)
btn2.pack(padx=120, pady=30)
btn4.pack(padx=120, pady=30)
root.mainloop()