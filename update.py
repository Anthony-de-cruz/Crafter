from tkinter import *

root = Tk()
root.geometry("100x100")


v = StringVar()
Label(root, textvariable=v).pack()

v.set("New Text!")

root.mainloop()
