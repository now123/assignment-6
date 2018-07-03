#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

from tkinter import *
myWindow= Tk()
myWindow.title("hello world")
lbl=Label(myWindow , text="hii world")
lbl.grid(column=0,row=0)
btn = Button(myWindow, text="Click Me",command=myWindow.destroy)
btn.grid(column=1, row=0)
myWindow.mainloop()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.
import tkinter
import tkinter as tk #for writing tk insted of tkinter
m=tkinter.Tk() #making container
m.title('countig Second')#for making tittle
def hi():
    print("hi johy hosins here")
btn = Button(m, text="clik",command =hi)
btn.pack()
m.mainloop()

# Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack(side=TOP)

middleFrame = Frame(root)
middleFrame.pack(side=RIGHT)

bottomFrame = Frame(root, bg="green")
bottomFrame.pack(side=BOTTOM)

topFrame_Label = Label(topFrame, text="welcome to deraming duo")
topFrame_Label.pack()
def background():

    var1 = StringVar()
    label1 = Label(topFrame, textvariable=var1)
    var1.set("welcome to dmaia-x")
    label1.pack()

theButton = Button(middleFrame, text="change", fg="red", bg="yellow",command=background)
theButton.pack()

theButton = Button(bottomFrame, text="exit", fg="red", bg="black",command=root.destroy)
theButton.pack()

root.mainloop()

#QUE 4- Write a python program using tkinter interface to take an input in the GUI program and print it.

from tkinter import *
import tkinter
import tkinter as tk
z=tk.Tk()
z.title("dancingmania")
l1=Label(z,text='name')
l1.grid(row=0)
e1=Entry(z)
e1.grid(row=0,column=3)
def tanuj():
    e=e1.get()
    print(e)
    z.destroy()
b1=Button(z,text='enter',width=25,command=tanuj)
b1.grid(row=4,column=4)

mainloop()
