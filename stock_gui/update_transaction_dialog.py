import logging
from tkinter import *
from tkinter.ttk import *
from stock_db.db_stock import StockTransactionTable, StockTransaction

class UpdateTransactionFrame(Frame):
    def __init__(self, master=None):
        self.master = master
        Frame.__init__(self, master)
        self.init_widget()

    def init_widget(self):
        self.scrollbar = Scrollbar(self)
        self.lstboxStockTransaction = Listbox(self)
        self.lstboxStockTransaction.grid(row = 0, column = 0, columnspan = 2)
        self.scrollbar.grid(row = 0, column = 3, sticky=NS)
        self.lstboxStockTransaction["yscrollcommand"] = self.scrollbar.set
        self.scrollbar["command"] = self.lstboxStockTransaction.yview
        self.refresh_list_box()

        self.entryAmount = Entry(self)
        self.entryAmount.grid(row = 1, column = 0, columnspan = 2)

        self.btnUpdate = Button(self)
        self.btnUpdate["text"] = "Update"
        self.btnUpdate.grid(row = 2, column = 0)
        self.btnUpdate["command"] = self.update_stock_transaction

        self.btnCancel = Button(self)
        self.btnCancel["text"] = "Cancel"
        self.btnCancel.grid(row = 2, column = 1)
        self.btnCancel["command"] = self.quit_dialog

        return

    def get_result(self):
        return 1000

    def update_stock_transaction(self):
        index = self.lstboxStockTransaction.curselection()
        if len(index) == 0:
            return

        stock_transaction = self.lstboxStockTransaction.get(index[0])

        print(stock_transaction.get_buy_or_sell())

        self.refresh_list_box()

        return

    def refresh_list_box(self):
        self.lstboxStockTransaction.delete(0, END)
        stock_transaction_table = StockTransactionTable()
        stock_transaction_list = \
            stock_transaction_table.get_all_stock_transaction()
        for stock_transaction in stock_transaction_list:
            self.lstboxStockTransaction.insert(END, \
                stock_transaction)
        return

    def quit_dialog(self):
        self.master.destroy()
        return

class UpdateTransactionDialog():
    def __init__(self, master=None):
        self.master = master
        self.root = None

    def open(self):
        self.root = Toplevel()
        self.frame = UpdateTransactionFrame(self.root)
        self.frame.grid(padx = 10, pady = 10)
        self.root.transient(self.master)
        self.root.grab_set()
        self.root.wait_window(self.root)
        result = self.frame.get_result()
        return result
