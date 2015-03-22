import logging
from tkinter import *

class NewCashPoolFrame(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.init_widget()

    def init_widget(self):
        self.lblSymbol = Label(self)
        self.lblSymbol["text"] = "Symbol:"
        self.lblSymbol.grid(row = 0, column = 0)

        self.lblAmount = Label(self)
        self.lblAmount["text"] = "Amount:"
        self.lblAmount.grid(row = 1, column = 0)

        self.entrySymbol = Entry(self)
        self.entrySymbol.grid(row = 0, column = 1)

        self.entryAmount = Entry(self)
        self.entryAmount.grid(row = 1, column = 1)

        self.btnAdd = Button(self)
        self.btnAdd["text"] = "Add"
        self.btnAdd.grid(row = 2, column = 0)

        self.btnCancel = Button(self)
        self.btnCancel["text"] = "Cancel"
        self.btnCancel.grid(row = 2, column = 1)
        self.btnCancel["command"] = self.hello
        
        return

    def get_result(self):
        return 1000
    
    def hello(self):
        print("hello world")
        self.master.destroy()
        
        
class NewCashPoolDialog():
    def __init__(self, master=None):
        self.master = master
        self.root = None

    def open(self):
        self.root = Toplevel()
        self.frame = NewCashPoolFrame(self.root)
        self.frame.grid(padx = 10, pady = 10)
        self.root.transient(self.master)
        self.root.grab_set()
        self.root.wait_window(self.root)
        result = self.frame.get_result()
        print("exit the window")
        return result
        
    
