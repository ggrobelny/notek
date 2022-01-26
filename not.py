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

Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
MidFrame = Frame(root, width=500)
MidFrame.pack(side=TOP)
LeftForm = Frame(MidFrame, width=100)
LeftForm.pack(side=LEFT)
RightForm = Frame(MidFrame, width=100)
RightForm.pack(side=RIGHT)

#==========================================================================================

lbl_title = Label(Top, width=500, font=('arial', 18), text="Python SQLite Search App")
lbl_title.pack(side=TOP, fill=X)
lbl_search = Label(LeftForm, font=('arial', 15), text="Search here...")
lbl_search.pack(side=TOP)

#==========================================================================================

search = Entry(LeftForm, textvariable=SEARCH)
search.pack(side=TOP, pady=10)

#==========================================================================================




if __name__=='__main__':
    root.mainloop()