import logging
from tkinter import *

class NewCashPoolFrame(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.init_widget()

    def init_widget(self):
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=4)
        self.columnconfigure(2, weight=5)
        self.rowconfigure(0, weight=2)
        self.rowconfigure(1, weight=3)
        self.rowconfigure(2, weight=3)
        self.button = Button(self)
        self.button["text"] = "This is a test"
        self.button["command"] = self.hello
        self.button.grid(row=1, column=1)

        self.button2 = Button(self)
        self.button2["text"] = "Button2"
        self.button2.grid(row=0, column=0)

        self.button3 = Button(self)
        self.button3["text"] = "Button3"
        self.button3.grid(row=2, column=2)

    def get_result(self):
        return 1000
    
    def hello(self):
        print("hello world in new frame")
        
        
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
        
    
