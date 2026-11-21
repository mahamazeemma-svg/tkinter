from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Virus Detected")
root.geometry("400x400")

def message():
    messagebox.showwarning("Virus Detected", "A virus has been detected on your system. Please take immediate action to remove it.")

btn = Button(root, text="Show Warning", command=message, bg="red")
btn.place(x=100, y=120)

root.mainloop()