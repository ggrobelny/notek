#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.log import error
from tkinter import *
import sqlite3
import tkinter.ttk as ttk
from os import system, name


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

root = Tk()
menubar= Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing, font=("Ubuntu", 10, "bold"), background="#34596b", foreground="#d6bf33")
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)




root.title('Notek')
width=1728
height=972
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2) - (width/2)
y=(screen_height/2) - (height/2)
error = Message(text="", width=160)
root.geometry("%dx%d+%d+%d" % (width,height,x,y))
root.resizable(0,0)
SEARCH = StringVar()


        

#==========================================================================================

def Database():
    conn = sqlite3.connect("testowe.db")
    cursor = conn.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS testy (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT) """)
    cursor.execute("SELECT * FROM testy")
    # if cursor.fetchone() is None:
    #     cursor.execute("INSERT INTO testy(title, content) VALUES ('title0', 'content0')")
    #     cursor.execute("INSERT INTO testy(title, content) VALUES ('title1', 'content1')")
    #     cursor.execute("INSERT INTO testy(title, content) VALUES ('title2', 'content2')")
    #     conn.commit()

    cursor.execute("SELECT * FROM testy ORDER BY content ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()        
    

def Search():
    if SEARCH.get() != "":
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("testowe.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM testy WHERE title LIKE ? OR content LIKE ?", ('%'+str(SEARCH.get())+'%', '%'+str(SEARCH.get())+'%'))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
            content.delete(1.0, END)
            content.insert(INSERT, data[2])
            
        cursor.close()
        conn.close()   


def Reset():
    conn = sqlite3.connect('testowe.db')
    cursor = conn.cursor()
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM testy ORDER BY content ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()


def fetchLastOne():
    conn = sqlite3.connect('testowe.db')
    pobierz = conn.cursor()
    pobierz.execute("SELECT content FROM testy ORDER BY id DESC LIMIT 1")
    dane = pobierz.fetchone()
    for dana in dane:
        print(dana, [0])
        content.delete("1.0",END)
        content.insert(INSERT, dana)


def addNewContent():
    conn = sqlite3.connect('testowe.db')
    cursor = conn.cursor()
    newTitle = title.get()
    newContent = content.get("1.0", END)

    cursor.execute("SELECT COUNT(*) FROM testy WHERE title='"+ newTitle +"' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Title already exists"
        
    else:
        error["text"] = "Added New Information"
        cursor.execute("INSERT INTO testy(title, content)VALUES(?,?)", (newTitle, newContent))   
        conn.commit()
        title.delete(0, END)
        content.delete(1.0, END)


def Clear():
    # windows
    if name=='nt':
        _=system('cls')

        # linux unix
    else:
        _=system('clear')
        search.delete(0,END)
        title.delete(0,END)
        content.delete(1.0,END)


#==========================================================================================

# def Menubar(self):
# 		self.menu = Menu(root, bd=2, background="#34596b", activebackground='#091b3a', activeforeground='#d6bf33')
# 		self.master.config(menu=self.menu)
# 		filemenu = Menu(self.menu, background="#a52a2a", activebackground='#091b3a', activeforeground='#d6bf33')
# 		self.menu.add_cascade(label="File", menu=filemenu, font=("Ubuntu", 10, "bold"), background="#34596b", foreground="#d6bf33")
# 		filemenu.add_command(label="New", command=self.NewFile, font=("Ubuntu", 10, "bold"), background="#34596b",
# 							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
# 		filemenu.add_command(label="Open", command=self.opn,font=("Ubuntu", 10, "bold"), background="#34596b",
# 							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
# 		filemenu.add_command(label="Save", command=self.save,font=("Ubuntu", 10, "bold"), background="#34596b",
# 							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
# 		filemenu.add_command(label="Save As..", command=self.saveas,font=("Ubuntu", 10, "bold"), background="#34596b",
# 							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
# 		filemenu.add_separator(background="#34596b")
# 		filemenu.add_command(label="Exit", command=self.quit, font=("Ubuntu", 10, "bold"), background="#a52a2a",
# 							 foreground="#d6bf33", activebackground='#091b3a', activeforeground='#d6bf33')
# 		filemenu.add_separator(background="#34596b")

#==========================================================================================

Top = Frame(root, width=900, height=1, bd=1, relief=SOLID)
Top.pack(side=TOP)
MidFrame = Frame(root, width=500)
MidFrame.pack(side=TOP)
LeftForm = Frame(MidFrame, width=100)
LeftForm.pack(side=LEFT)
RightForm = Frame(MidFrame, width=500)
RightForm.pack(side=RIGHT)

#==========================================================================================

lblTitle = Label(width=1250, font=('arial', 18), text="Python SQLite Search App")
lblTitle.pack(side=TOP, fill=X)
lblSearch = Label(font=('arial', 15), text="Search here...")
lblSearch.pack(side=TOP, anchor=E)
title = Entry(text="")
title.place(x=300, y=100)
title.config(bg='cyan')

#==========================================================================================

search = Entry(textvariable=SEARCH)
search.pack(side=TOP, anchor=E)
search.config(bg='lightgreen')

#==========================================================================================

content = Text(root)
content.place(x=300, y=150, width=575, height=600)
content.config(bg='cyan')

#==========================================BUTTON AREA================================================

btnSearch = Button(text="Search", bg="#006dcc", command=Search)
btnSearch.pack(side=LEFT, anchor=N)
btnSearch.place(x=75, y=50)
btnReset = Button(text="Reset", command=Reset)
btnReset.pack(side=LEFT, anchor=NW)
btnReset.place(x=10, y=50)
btnLast = Button(text="LastID", bg="lightgreen", command=fetchLastOne)
btnLast.place(x=140, y=50)
btnInsert = Button(text="Wsad", bg="lightgreen", command=addNewContent)
btnInsert.place(x=30, y=800)
btnClear = Button(text="Clear", bg="lightgreen", command=Clear)
btnClear.place(x=100, y=800)

#==========================================================================================

scrollbarx = Scrollbar(orient=HORIZONTAL)
scrollbary = Scrollbar(orient=VERTICAL)
tree = ttk.Treeview(columns=("MemberID", "Title", "Content"), selectmode="extended", height=400, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID")
tree.heading('Content', text="Content")
tree.heading('Title', text="Title")

tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=150)
tree.column('#3', stretch=NO, minwidth=0, width=0)
tree.pack(anchor=E)


#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================


if __name__=='__main__':
    Database()


root.config(menu=menubar)
root.mainloop()