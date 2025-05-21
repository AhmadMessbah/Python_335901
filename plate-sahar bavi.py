# pip install pillow

from tkinter import *
from PIL import Image, ImageTk

def open_new_form():
    window.destroy()
    new_form = Tk()
    new_form.mainloop()

window = Tk()
window.title("Person Info")
window.geometry("1250x300")

# Id
img = Image.open("plate.jpg")
# img = img.resize((76, 26))

img = ImageTk.PhotoImage(img)

my_label = Label(window, image=img)
my_label.place(x=20, y=20)

# Button(window, image=img,command=open_new_form).place(x=20, y=200)
part1 = StringVar(value = "12")
Entry(window, textvariable=part1,width=2, font=("B Traffic", 120)).place(x=140,y=50, height=220 , width=200)

part2 = StringVar(value = "ب")
Entry(window, textvariable=part2,width=2, font=("B Traffic", 120)).place(x=350,y=50,  height=220 , width=200)

part3 = StringVar(value = "123")
Entry(window, textvariable=part3,width=2, font=("B Traffic", 120)).place(x=530,y=50,  height=220 , width=400)

part4 = StringVar(value = "12")
Entry(window, textvariable=part4,width=2, font=("B Traffic", 120)).place(x=960,y=98,  height=180 , width=198)

part1.get()
part2.get()
part3.get()
part4.get()

window.mainloop()
