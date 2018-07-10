from tkinter import*
root=Tk("Text Editor")
root.title("Text Editor")
text=Text(root)
text.grid()


def donothing():
    file = Toplevel(root)
    button = Button(file, text="abhi kuch nhi")
    button.pack()


menubar = Menu(root)
#adding the menus <1> file
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New   ctrl+n", command=donothing)
filemenu.add_command(label="Open  ctrl+o", command=donothing)
filemenu.add_command(label="Save  ctrl+s", command=donothing)
filemenu.add_command(label="Save as", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#adding the menu <2>edit


editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="cut  ctrl+x", command=donothing)
editmenu.add_command(label="copy ctrl+c", command=donothing)
editmenu.add_command(label="paste ctrl+v", command=donothing)
editmenu.add_command(label="delete", command=donothing)

#adding menu<3> view
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="View", menu=viewmenu)
viewmenu.add_command(label="status", command=donothing)
viewmenu.add_command(label="recent file", command=donothing)
viewmenu.add_command(label="toolbar", command=donothing)

#adding menu<4> about
viewmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About", menu=viewmenu)
viewmenu.add_command(label="info", command=donothing)
viewmenu.add_command(label="help", command=donothing)
root.config(menu=menubar)
root.mainloop()