from tkinter import *

root = Tk()
root.title("logging app")
root.geometry("400x400")

frame = Frame(root, height=200, width=360, bg="lightblue")

lbl1 = Label(frame, text="fullname:" , bg="blue", fg="white")
lbl2 = Label(frame, text="email:" , bg="blue", fg="white")
lbl3 = Label(frame, text="password:" , bg="blue", fg="white")

name_entry = Entry(frame)
email_entry = Entry(frame)
password_entry = Entry(frame, show="*")

def display():
    name = name_entry.get()
    global Message
    Message = "welcome to the application"
    greet = "hello " + name + " " + Message
    textbox.insert(END, greet)

textbox = Text(root, bg="grey", fg="black")

btn = Button(root, text="create account", command=display, bg="red")

frame.place(x=20, y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=100, y=20)
lbl2.place(x=20, y=60)
email_entry.place(x=100, y=60)
lbl3.place(x=20, y=100)
password_entry.place(x=100, y=100)
btn.place(x=130, y=150)
textbox.place(y = 250)

root.mainloop()
