
from tkinter import *
from PIL import Image, ImageTk


def open_new_form():
    window.destroy()
    new_form = Tk()
    new_form.mainloop()


window = Tk()
window.title("Person Info")
window.geometry("900x300")

img = Image.open("plate.jpg")
img = ImageTk.PhotoImage(img)

my_label = Label(window, image=img)
my_label.place(x=20, y=20)

part1 = IntVar()
Entry(window, textvariable=part1, width=2, font=("B Traffic", 120)).place(x=150, y=100, height=150)
part2 = StringVar()
Entry(window, textvariable=part2, width=2, font=("B Traffic", 120)).place(x=350, y=100, height=150)
part3 = IntVar()
Entry(window, textvariable=part3, width=4, font=("B Traffic", 120)).place(x=550, y=100, height=150)
part4 = IntVar()
Entry(window, textvariable=part4, width=3, font=("B Traffic", 120)).place(x=950, y=100, height=150)

part1.get()
part2.get()
part3.get()
part4.get()
window.mainloop()