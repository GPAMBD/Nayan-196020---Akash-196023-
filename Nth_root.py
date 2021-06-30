from tkinter import *
import math


def findRoot():
    eps = 1e-4
    csquare = float(input(square.get()))
    cn = int(input(n.get()))
    


    max = csquare * 1.0
    min = 1.0
    mid = 0.0

    while max - min > eps:
        mid = (max + min) / 2
        if pow(mid, cn) < csquare:
            min = mid
        else:
            max = mid

    min = round(min, 3)



    label1 = Label(window, text='Square Root of ' + square.get() + ' = ' + str(min), fg='green', font=('Arial', 14))
    label1.place(x=15, y=250)


window = Tk()
window.geometry('500x400')

heading = Label(window, text='Nth ROOT FINDER', bg='yellow', font=('Arial', 16))
heading.place(x=200, y=0)

square = StringVar()
n = StringVar()

label = Label(window, text='Enter a number : ', font=('Arial', 14))
label.place(x=100, y=50)

input_square = Entry(window, textvariable=square)
input_square.place(x=300, y=50)

label = Label(window, text='Enter N for Nth root : ', font=('Arial', 14))
label.place(x=100, y=100)

input_n = Entry(window, textvariable=n)
input_n.place(x=300, y=100)

button = Button(window, command=findRoot, text='SQUARE ROOT', fg='green', font=('Arial', 14))
button.place(x=175, y=150)

window.mainloop()