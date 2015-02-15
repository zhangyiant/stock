import logging
from tkinter import *

class StockApp:
    def __init__(self):
        self.root = Tk()
        self.init_stock_cash_menu()
    
    def init_stock_cash_menu(self):
        self.cash_menu = Menu(self.root)
        self.cash_menu.add_command(label="Hello!", command=self.hello)
        self.cash_menu.add_command(label="Quit!", command=self.root.quit)
        self.root["menu"] = self.cash_menu

    def hello(self):
        print("Hello!")

    def mainloop(self):
        self.root.mainloop()


