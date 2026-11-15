from tkinter import *

root = Tk()
root.title("Number pad")
root.geometry("250x300")

num = [[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]

for i in range(4):
    root.columnconfigure(i, weight=1)
    root.rowconfigure(i, weight=1)

    for j in range(0,3):
        frame = Frame(root, relief=RAISED, borderwidth=1)
        frame.grid(row=i, column=j)
        label = Label(frame, text=num[i][j], font=("Arial", 20))
        label.pack()

root.mainloop()