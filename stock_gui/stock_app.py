import logging
from tkinter import *
from stock_db.db_connection import get_default_db_connection
from stock_gui.new_cash_pool_dialog import NewCashPoolDialog
from stock_gui.show_cash_pool_dialog import ShowCashPoolDialog
from stock_gui.del_cash_pool_dialog import DelCashPoolDialog

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
                                   command=self.del_cash_pool)
        self.cash_menu.add_command(label="Update cash pool...",
                                   command=donothing)
        self.cash_menu.add_command(label="Show cash pool...",
                                   command=self.show_cash_pool)
        self.menu_bar.add_cascade(label="Cash", menu=self.cash_menu)

        self.other_menu.add_command(label="new quit!", command=self.root.quit)
        self.other_menu.add_command(label="Reset database",
                                    command=self.reset_db)
        self.menu_bar.add_cascade(label="other", menu=self.other_menu)

        self.root["menu"] = self.menu_bar

    def init_widget(self):
        self.button = Button(self.root)
        self.button["text"] = "hello world"
        self.button.pack()
        return
    
    def new_cash_pool(self):
        dialog = NewCashPoolDialog()
        result = dialog.open()
        return

    def del_cash_pool(self):
        dialog = DelCashPoolDialog()
        result = dialog.open()
        return

    def show_cash_pool(self):
        dialog = ShowCashPoolDialog()
        result = dialog.open()
        return

    def reset_db(self):
        db_conn = get_default_db_connection()
        db_conn.reset_table()
        return

    def mainloop(self):
        self.root.mainloop()
        return
