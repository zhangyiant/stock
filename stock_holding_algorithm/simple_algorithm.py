from stock_db.db_stock import StockCashTable, StockCash
from stock_db.db_stock import StockTransactionTable, StockTransaction
from stock_db.db_connection import get_default_db_connection

class simple_algorithm:
    def __init__(self, start_price = None, stop_price = None,
                 current_price = None, conn = None):
        if conn == None:
            self.conn = get_default_db_connection()
        else:
            self.conn = conn
        self.start_price = start_price
        self.stop_price = stop_price
        self.current_price = current_price

    def get_start_price():
        return self.start_price

    def get_stop_price():
        return self.stop_price

    def get_current_price():
        return self.current_price

    def get_connection():
        return self.conn

    def set_start_price(start_price):
        self.start_price = start_price
        return

    def set_stop_price(stop_price):
        self.stop_price = stop_price
        return

    def set_current_price(current_price):
        self.current_price = current_price
        return

    def set_connection(conn):
        self.conn = conn
        return

    def get_percentage(self, current_price):
        if current_price < self.start_price:
            return 0
        if current_price > self.start_price:
            return 100

    def __str__(self):
        result = ""
