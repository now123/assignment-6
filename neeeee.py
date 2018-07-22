from tkinter import *
import os
from tkinter import Tk,scrolledtext ,Menu,filedialog, messagebox , simpledialog, Text
import tkinter.scrolledtext as ScrolledText
import tkinter.filedialog
import tkinter.messagebox
import urllib
from PIL import ImageTk, Image

#root for main window
root = Tk(className=" Text Editor")
textArea = ScrolledText.ScrolledText(root,width=100,height=500)
root.iconbitmap('icons/favicon (1).ico')
#root.geometry('800*550')
#FUNCTIONS OF FILE

#FILE MENU

def new_file():
    if len(textArea.get("1.0",END+'-1c'))>0:
        if messagebox.askyesno("Save","Do you want to save ?"):
            save()
    else:
        textArea.delete("1.0",END)

def open_file():
    file= filedialog.askopenfile(parent=root,title='Select a text file', filetypes=(("Text file","*.txt"), ("All files","*.*")))
    if file !=None:
        contents = file.read()
        textArea.insert('1.0',contents)
        file.close()

def save():
    file= filedialog.asksaveasfile(mode='w')
    if file !=None:
        data= textArea.get('1.0',END+'-1c')
        file.write(data)
        file.close()

def saveas():
    file = filedialog.asksaveasfile(mode='w',defaultextension='.text')
    text = textArea.get('1.0',END)
    try:
        file.write(text.strip())
    except():
        showerror(title="oops!", message="Unable to save file")



def FindInFile():
    FindString = simpledialog.askstring("Find...", "Enter text")
    textdata = textArea.get("1.0", END)

    occurances = textdata.upper().count(FindString.upper())

    if textdata.upper().count(FindString.upper())>0:
        label= messagebox.showinfo("Results",FindString + "has multiple occurances," +str(occurances))
    else:
        label = messagebox.showinfo("Result", "sorry nothing to show")

    print(textdata)

def exit():
    if messagebox.askyesno("Quit","Are you sure you want to quit"):
        root.destroy()

#ABOUT MENU

def Aboutroot():
    label= messagebox.showinfo("About", "A Python alternative to Notepad++")

#HELP MENU
def helproot():
    label= messagebox.showinfo("HELP", "This text editor works similiar to any other text editors")

#EDIT MENU
def cut(event=None):
    content_text.event_generate("<<Cut>>")
    on_content_changed()
    return "break"

def copy(event=None):
    content_text.event_generate("<<Copy>>")
    on_content_changed()
    return "break"

def paste(event=None):
    content_text.event_generate("<<Paste>>")
    on_content_changed()
    return "break"

def undo(event= None):
    content_text.event_generate("<<Undo>>")
    on_content_changed()
    return "break"

def redo(event=None):
    content_text.event_generate("<<Redo>>")
    on_content_changed()
    return "break"

def selectall(event=None):
    content_text.tag_add('SelectAll', '1.0', 'end')
    on_content_changed()
    return "break"
def deleteall(event=None):
    textArea.tag_add('DeleteAll','1.0','end')
    return "break"

###################################################################################################
#LINE NUMBER FUNCTION

def get_line_number():
    output=' '
    if show_line_number.get():
        row,col=content_text.index("end").split('.')
        for i in range(1,int(row)):
            output += str(i)+'\n'
    return output

def on_content_changed(event=None):
    update_line_numbers()
    update_cursor()

def update_line_numbers(event=None):
    line_numbers = get_line_number()
    line_number_bar.config(state='normal')
    line_number_bar.delete('1.0','end')
    line_number_bar.insert('1.0',line_numbers)
    line_number_ba
    r.config(state='disabled')

#ADDING CURSOR FUNCTIONALITY
def show_cursor():
    show_cursor_info_checked= show_cursor_info.get()
    if show_cursor_info_checked:
        cursor_info_bar.pack(expand='yes',fill=None,side='right',anchor='se')
    else:
        cursor_info_bar.pack_forgot()

def update_cursor(event=None):
    row, col = content_text.index(INSERT).split('.')
    line_num, col_num= str(int(row)),str(int(col)+1)
    infotext ="Line:{0}| Column:{1}".format(line_num,col_num)
    cursor_info_bar.config(text=infotext)

#ADDING TEXT HIEGLIGHT FUNCTIONALLTY

def highlight_line(interval=100):
    content_text.tag_remove("active_line", 1.0,"end")
    content_text.tag_add("active_line", "insert linestart", "insert lineend+1c")
    content_text.after(interval,toggle_highlight)
def undo_highlight():
    content_text.tag_remove("active_line", 1.0,"end")
def toggle_highlight(event=None):
    if to_highlight_line.get():
        highlight_line()
    else:
        undo_highlight()

#THEME FUNCTIONALITY

def change_theme(event=None):
    selected_theme = theme_choice.get()
    fg_bg_colors = color_schemes.get(selected_theme)
    foreground_color, background_color= fg_bg_colors.split('.')
    content_text.config(background_color, fg=foreground_color)

#POPUP MENU

def show_popup_menu(event):
    popup_menu.tk_popup(event.x_root, event.y_root)


#ICONS  CODE
new_File_icon = PhotoImage(file='icons/new_file.gif')
open_File_icon = PhotoImage(file='icons/open_file.gif')
save_File_icon = PhotoImage(file='icons/save.gif')
cut_icon = PhotoImage(file='icons/cut.gif')
copy_icon = PhotoImage(file='icons/copy.gif')
paste_icon = PhotoImage(file='icons/paste.gif')
undo_icon = PhotoImage(file='icons/undo.gif')
redo_icon = PhotoImage(file='icons/redo.gif')


#FILE MENU OPTIONS
menu=Menu(root)
root.config(menu=menu)
filemenu=Menu(menu,tearoff=0)
menu.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='New',command=new_file,accelerator="Ctrl+N",compound='left', image=new_File_icon, underline=0)
filemenu.add_command(label='Open', command=open_file,accelerator="Ctrl+O",compound='left', image=open_File_icon, underline=0)
filemenu.add_command(label='Save', command=save,accelerator="Ctrl+S",compound='left', image=save_File_icon, underline=0)
filemenu.add_command(label='Save As',command=saveas,accelerator="Ctrl+Alt+S",compound='left', underline=0)
filemenu.add_command(label='Find', command=FindInFile,accelerator="Ctrl+F",compound='left', underline=0)
filemenu.add_command(label='Print',accelerator="Ctrl+P",compound='left',underline=0)
filemenu.add_separator()
filemenu.add_command(label='Exit',command=exit,accelerator="Ctrl+E",compound='left',underline=0)

#END OF FILE MENU OPTION

#EDIT MENU OPTIONS
editmenu = Menu(menu,tearoff=0)
menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label="Cut",command=cut, accelerator="Ctrl+X",compound='left', image=cut_icon, underline=0)
editmenu.add_command(label="Copy", command=copy, accelerator="Ctrl+C",compound='left', image=copy_icon,underline=0)
editmenu.add_command(label="Paste", command=paste, accelerator="Ctrl+V",compound='left', image=paste_icon, underline=0)
editmenu.add_command(label="Undo", command=undo,accelerator="Ctrl+Z",compound='left', image=undo_icon, underline=0)
editmenu.add_command(label="Redo", command=redo, accelerator="Ctrl+Y",compound='left',image=redo_icon, underline=0)
editmenu.add_command(label="SelectAll", command=selectall, accelerator="Ctrl+A",compound='left',underline=0)
editmenu.add_command(label="DeleteAll", command=deleteall)
root.configure(menu=menu)

#VIEW MENUBAR OPTIONS

view_menu = Menu(menu, tearoff=0)
show_line_number = IntVar()
show_line_number.set(1)
view_menu.add_checkbutton(label="Show Line Number", variable=show_line_number)
show_cursor_info = IntVar()
show_cursor_info.set(1)
view_menu.add_checkbutton(label='Show Cursor Location at Down', variable=show_cursor_info, command=show_cursor)
to_highlight_line = IntVar()
view_menu.add_checkbutton(label='Highlight Current Line', variable=to_highlight_line, onvalue=1, offvalue=0,command=toggle_highlight)
themes_menu = Menu(menu, tearoff=0)
view_menu.add_cascade(label='Themes', menu=themes_menu, command=change_theme)

root.config(menu=menu)

# THEMES OPTIONS
color_schemes = {'Default': '#000000.#FFFFFF',
                 'Greygarious': '#83406A.#D1D4D1',
                 'Aquamarine': '#5B8340.#D1E7E0',
                 'Bold Beige': '#4B4620.#FFF0E1',
                 'Cobalt Blue': '#ffffBB.#3333aa',
                 'Olive Green': '#D1E7E0.#5B8340',
                 'Night Mode': '#FFFFFF.#000000',}

theme_choice = StringVar()
theme_choice.set('Default')
for k in sorted(color_schemes):
    themes_menu.add_radiobutton(label=k, variable=theme_choice, command=change_theme)

menu.add_cascade(label='View', menu=view_menu)

##ABOUT MENUBAR

about_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='About', menu=about_menu)
about_menu.add_command(label='About', underline=0, command=Aboutroot)
about_menu.add_command(label='Help', underline=0, command=help)

#END OF ABOUT MENUBAR

root.config(menu=menu)

icon_frame=Frame(root,height=80)
icon_frame.pack(expand='no',fill='x')


icons=('new_file','open_file','save','cut','copy','paste','undo','redo')
for i, icon in enumerate(icons):
    tool_bar_icon = PhotoImage(file='icons/{}.gif'.format(icon)).zoom(2,2)
    cmd = eval(icon)
    tool_bar = Button(icon_frame, image=tool_bar_icon, height=15,width=15,command=cmd)
    tool_bar.image = tool_bar_icon
    tool_bar.pack(side='left')

line_number_bar = Text(root, width=4, padx=3, takefocus=0, fg='white', border=0, background='#282828', state='disabled',
                       wrap='none')
line_number_bar.pack(side='left', fill='y')

#Main Context Text widget and Scrollbar Widget
content_text = Text(root, wrap='word')
content_text.pack(expand='yes', fill='both')

scroll_bar = Scrollbar(content_text)
content_text.configure(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=content_text.yview)
scroll_bar.pack(side='right', fill='y')

# ADDING CURSOR INFO LABEL
cursor_info_bar = Label(content_text, text='Line: 1 | Column: 1')
cursor_info_bar.pack(expand='no', fill=None, side='right', anchor='se')

#SETTING THE POPUP MENU
popup_menu = Menu(content_text)
for i in ('cut', 'copy', 'paste', 'undo', 'redo'):
    cmd = eval(i)
    popup_menu.add_command(label=i, compound='left', command=cmd)
popup_menu.add_separator()
popup_menu.add_command(label='Select All', underline=7, command=selectall)
content_text.bind('<Button-3>', show_popup_menu)

#HANDLING BINDING

'''content_text.bind('<Control-N>', new_file)
content_text.bind('<Control-n>', new_file)
content_text.bind('<Control-O>', open_file)
content_text.bind('<Control-o>', open_file)
content_text.bind('<Control-S>', save)
content_text.bind('<Control-s>', save)
content_text.bind('<Control-Y>',redo)
content_text.bind('<Control-y>',redo)
content_text.bind('<Control-A>',selectall)
content_text.bind('<Control-a>',selectall)
content_text.bind('<Control-F>',find_text)
content_text.bind('<Control-f>',find_text)
content_text.bind('<KeyPress-F1>', display_help)
content_text.bind('<Any-KeyPress>', on_content_changed)
content_text.tag_configure('active_line', background='ivory2')
content_text.bind('<Button-3>', show_popup_menu)
content_text.focus_set()'''

# END OF MENU

root.protocol('WM_DELETE_WINDOW', exit)
root.mainloop()