from tkinter import *
import sqlite3
import tkinter.ttk as ttk

root = Tk()
root.title('Notek')
width=1250
height=700
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
x=(screen_width/2) - (width/2)
y=(screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width,height,x,y))
root.resizable()
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

#==========================================================================================

Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
MidFrame = Frame(root, width=500)
MidFrame.pack(side=TOP)
LeftForm = Frame(MidFrame, width=100)
LeftForm.pack(side=LEFT)
RightForm = Frame(MidFrame, width=500)
RightForm.pack(side=RIGHT)

#==========================================================================================

lblTitle = Label(Top, width=1250, font=('arial', 18), text="Python SQLite Search App")
lblTitle.pack(side=TOP, fill=X)
lblSearch = Label(LeftForm, font=('arial', 15), text="Search here...")
lblSearch.pack(side=TOP)

#==========================================================================================

search = Entry(LeftForm, textvariable=SEARCH)
search.pack(side=TOP, pady=10)

#==========================================================================================

btnSearch = Button(LeftForm, text="Search", bg="#006dcc", command=Search)
btnSearch.pack(side=LEFT)
btnReset = Button(LeftForm, text="Reset", command=Reset)
btnReset.pack(side=LEFT)

#==========================================================================================

scrollbarx = Scrollbar(RightForm, orient=HORIZONTAL)
scrollbary = Scrollbar(RightForm, orient=VERTICAL)
tree = ttk.Treeview(RightForm, columns=("MemberID", "Title", "Content"), selectmode="extended", height=400, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('Title', text="Title", anchor=W)
tree.heading('Content', text="Content")
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=380)
tree.column('#3', stretch=NO, minwidth=0, width=700)
tree.pack()

#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================


if __name__=='__main__':
    Database()
    root.mainloop()