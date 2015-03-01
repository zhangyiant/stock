import logging
from tkinter import *

class NewCashPoolFrame(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.init_widget()

    def init_widget(self):
        self.button = Button(self)
        self.button["text"] = "This is a test"
        self.button["command"] = self.hello
        self.button.pack()

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
        self.frame.pack()
        self.root.transient(self.master)
        self.root.grab_set()
        self.root.wait_window(self.root)
        result = self.frame.get_result()
        print("exit the window")
        return result
        
    
