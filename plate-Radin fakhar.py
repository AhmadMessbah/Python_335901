# pip install pillow

from tkinter import *
from PIL import Image, ImageTk

def check_plate():
    print(part1.get(), part2.get())

window = Tk()
window.title("Person Info")
window.geometry("1300x400")

# Id
img = Image.open("plate.jpg")
# img = img.resize((76, 26))

img = ImageTk.PhotoImage(img)

my_label = Label(window, image=img)
my_label.place(x=20, y=20)


part1 = StringVar(value = "12")
Entry(window, textvariable=part1,width=2, font=("B Traffic", 160)).place(x=140,y=50, height=225)

part2 = StringVar(value = "ب")
Entry(window, textvariable=part2,width=2, font=("B Traffic", 180)).place(x=350,y=50, height=225)

part3 = StringVar(value = "345")
Entry(window, textvariable=part3,width=3, font=("B Traffic", 180)).place(x=560,y=50, height=225)

part4 = StringVar(value = "11")
Entry(window, textvariable=part4,width=2, font=("B Traffic", 180)).place(x=950,y=50, height=225)

Button(window, text="Save",command=check_plate).place(x=20, y=350)
window.mainloop()
