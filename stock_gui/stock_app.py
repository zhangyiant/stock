import logging
from tkinter import *
from stock_gui.new_cash_pool_dialog import NewCashPoolDialog
from stock_gui.show_cash_pool_dialog import ShowCashPoolDialog

def donothing():
    return

class StockApp:
    def __init__(self):
        self.root = Tk()
        self.init_stock_cash_menu()
        self.init_widget()
    
    def init_stock_cash_menu(self):
        self.menu_bar = Menu(self.root)
        self.cash_menu = Menu(self.menu_bar)
        self.other_menu = Menu(self.menu_bar)

        self.cash_menu.add_command(label="New cash pool...",
                                   command=self.new_cash_pool)
        self.cash_menu.add_command(label="Delete cash pool...",
                                   command=donothing)
        self.cash_menu.add_command(label="Update cash pool...",
                                   command=donothing)
        self.cash_menu.add_command(label="Show cash pool...",
                                   command=self.show_cash_pool)
        self.menu_bar.add_cascade(label="Cash", menu=self.cash_menu)

        self.other_menu.add_command(label="new quit!", command=self.root.quit)
        self.other_menu.add_command(label="hello", command=self.hello)
        self.menu_bar.add_cascade(label="other", menu=self.other_menu)

        self.root["menu"] = self.menu_bar

    def init_widget(self):
        self.button = Button(self.root)
        self.button["text"] = "hello world"
        self.button.pack()
        self.button["command"] = self.hello2

    def new_cash_pool(self):
        dialog = NewCashPoolDialog()
        result = dialog.open()
        print(result)

    def show_cash_pool(self):
        dialog = ShowCashPoolDialog()
        result = dialog.open()
        print(result)
        
    def hello(self):
        self.p = Toplevel()
        self.p.transient(self.root)
        self.p.grab_set()
        print("hello")

    def hello2(self):
        print("hello2")
    def mainloop(self):
        self.root.mainloop()


