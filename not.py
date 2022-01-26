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
root.resizable(0,0)
SEARCH = StringVar()

#==========================================================================================

def Search():
    print("")

def Reset():
    print("")

#==========================================================================================

Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
MidFrame = Frame(root, width=500)
MidFrame.pack(side=TOP)
LeftForm = Frame(MidFrame, width=100)
LeftForm.pack(side=LEFT)
RightForm = Frame(MidFrame, width=100)
RightForm.pack(side=RIGHT)

#==========================================================================================

lblTitle = Label(Top, width=500, font=('arial', 18), text="Python SQLite Search App")
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

#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================

#==========================================================================================


if __name__=='__main__':
    root.mainloop()