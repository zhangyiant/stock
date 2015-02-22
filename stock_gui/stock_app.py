import logging
from tkinter import *

def donothing():
    return

class StockApp:
    def __init__(self):
        self.root = Tk()
        self.init_stock_cash_menu()
    
    def init_stock_cash_menu(self):
        self.menu_bar = Menu(self.root)
        self.cash_menu = Menu(self.menu_bar)
        self.other_menu = Menu(self.menu_bar)

        self.cash_menu.add_command(label="New cash pool...", command=donothing)
        self.cash_menu.add_command(label="Delete cash pool...", command=donothing)
        self.cash_menu.add_command(label="Update cash pool...", command=donothing)
        self.menu_bar.add_cascade(label="Cash", menu=self.cash_menu)

        self.other_menu.add_command(label="new quit!", command=self.root.quit)
        self.menu_bar.add_cascade(label="other", menu=self.other_menu)

        self.root["menu"] = self.menu_bar

    def hello(self):
        print("Hello!")

    def mainloop(self):
        self.root.mainloop()


