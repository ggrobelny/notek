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

#================================================================================

Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)

if __name__=='__main__':
    root.mainloop()