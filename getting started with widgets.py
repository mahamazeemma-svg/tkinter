from tkinter import *
from datetime import date

root = Tk()
root.title("Getting Started with Widgets")
root.geometry("400x300")

lbl = Label(root, text="Hey there", fg="white", bg="black", font=("Arial", 16))

name_lbl = Label(root, text="Enter your name:")
name_entry = Entry()
def display():
    name = name_entry.get()
    global Message
    Message = "welcome to the application"
    greet = "hello " + name + " " + Message
    textbox.insert(END, greet)

textbox = Text(root, height=5, width=30)

btn = Button(root, text="Submit", command=display)

lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
textbox.pack()

root.mainloop()
