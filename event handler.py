from tkinter import *

window = Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print("Key pressed:", event.char)

window.bind("<Key>", handle_keypress)

def handle_button_click(event):
    print("Button clicked!")

btn = Button( text="Click Me")
btn.pack()

btn.bind("<Button-1>", handle_button_click)

window.mainloop()