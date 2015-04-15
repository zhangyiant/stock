import logging
from tkinter import *
from tkinter.ttk import *
from stock_db.db_stock import StockCashTable, StockCash
from stock_db.db_stock import StockTransactionTable, StockTransaction

class SuggestionFrame(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.init_widget()

    def init_widget(self):

        self.lblSymbol = Label(self)
        self.lblSymbol["text"] = "Symbol:"
        self.lblSymbol.grid(row = 0, column = 0)

        self.cbbSymbol = Combobox(self)
        self.fill_symbol_combobox()
        self.cbbSymbol.grid(row = 0, column = 1)

        self.btnSuggest = Button(self)
        self.btnSuggest["text"] = "Suggest"
        self.btnSuggest.grid(row = 1, column = 0)
        self.btnSuggest["command"] = self.suggest_stock()

        self.btnCancel = Button(self)
        self.btnCancel["text"] = "Cancel"
        self.btnCancel.grid(row = 1, column = 1)
        self.btnCancel["command"] = self.quit_dialog

        return

    def get_result(self):
        return 1000

    def fill_symbol_combobox(self):
        stock_cash_table = StockCashTable()
        stock_cash_list = stock_cash_table.get_all_stock_cash()
        symbol_list = []
        for stock_cash in stock_cash_list:
            symbol_list.append(stock_cash.get_symbol())
        self.cbbSymbol["values"] = symbol_list
        return

    def suggest_stock(self):
        return

    def quit_dialog(self):
        self.master.destroy()
        return

class SuggestionDialog():
    def __init__(self, master=None):
        self.master = master
        self.root = None

    def open(self):
        self.root = Toplevel()
        self.frame = SuggestionFrame(self.root)
        self.frame.grid(padx = 10, pady = 10)
        self.root.transient(self.master)
        self.root.grab_set()
        self.root.wait_window(self.root)
        result = self.frame.get_result()
        return result
