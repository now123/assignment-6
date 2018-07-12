from tkinter import*
import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

root=Tk("Text Editor")
root.title("Text Editor")
text=Text(root)
# To add scrollbar

scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

def donothing():
    file = Toplevel(root)
    button = Button(file, text="abhi kuch nhi")
    button.pack()

####
def about():
    showinfo("Notepad", "welcome to my world")


def opn():
    text.delete(1.0, END)

    file = open(askopenfilename(), 'r')

    if file != '':

        txt = file.read()

        text.insert(INSERT, txt)

    else:

        pass


def save():
    filename = asksaveasfilename()

    if filename:
        alltext =text.get(1.0, END)

        open(filename, 'w').write(alltext)


def copy():
    text.clipboard_clear()

    text.clipboard_append(text.selection_get())


def paste():
    try:

        teext = text.selection_get(selection='CLIPBOARD')

        text.insert(INSERT, teext)

    except:

        tkMessageBox.showerror("Error", "can't be done!")



menubar = Menu(root)
#adding the menus <1> file
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",font="ariel 20", menu=filemenu)
filemenu.add_command(label="New   ctrl+n", command=donothing)
filemenu.add_command(label="Open  ctrl+o", command=opn)
filemenu.add_command(label="Save  ctrl+s", command=save)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#adding the menu <2>edit


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="cut  ctrl+x", command=donothing)
editmenu.add_command(label="copy ctrl+c", command=copy)
editmenu.add_command(label="paste ctrl+v", command=paste)
editmenu.add_command(label="delete", command=donothing)

#adding menu<3> view
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="status", command=donothing)
viewmenu.add_command(label="recent file", command=donothing)

#adding menu<4> about
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=viewmenu)
viewmenu.add_command(label="info", command=about)
root.config(menu=menubar)
root.mainloop()