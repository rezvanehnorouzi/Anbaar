import tkinter as tk
from tkinter import Tk
from tkinter.ttk import Combobox,Treeview
import tkinter.messagebox  as mb
from Database import Resource

class Panel(Tk):
    resource = Resource() 
    def __init__(self):
        super().__init__()
        self.screencenter = (self.winfo_screenwidth()/2,
                             self.winfo_screenheight()/2)
        self.title("انبار دار")
        self.update_idletasks()
        self.size = tuple(int(_)
                          for _ in self.geometry().split('+')[0].split('x'))
        self.geometry(
            "+%d+%d" % (self.screencenter[0]-self.size[0]/2, self.screencenter[1]-self.size[1]))
        self.widget()
    def widget(self):
        pass