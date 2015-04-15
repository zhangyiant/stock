from stock_db.db_stock import StockCashTable, StockCash
from stock_db.db_stock import StockTransactionTable, StockTransaction
from stock_db.db_connection import get_default_db_connection

class simple_algorithm:
    def __init__(self, symbol = None, start_price = None, stop_price = None,
                 current_price = None, conn = None):
        if conn == None:
            self.conn = get_default_db_connection()
        else:
            self.conn = conn
        self.symbol = symbol
        self.start_price = start_price
        self.stop_price = stop_price
        self.current_price = current_price
        self.suggested_buy_or_sell = None
        self.suggested_amount = 0

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def get_start_price(self):
        return self.start_price

    def get_stop_price(self):
        return self.stop_price

    def get_current_price(self):
        return self.current_price

    def get_connection(self):
        return self.conn

    def set_start_price(self, start_price):
        self.start_price = start_price
        return

    def set_stop_price(self, stop_price):
        self.stop_price = stop_price
        return

    def set_current_price(self, current_price):
        self.current_price = current_price
        return

    def set_connection(self, conn):
        self.conn = conn
        return

    def calculate(self):
        self.suggested_buy_or_sell = "buy"
        self.suggested_amount = 100
        return

    def get_suggested_buy_or_sell(self):
        return self.suggeted_buy_or_sell

    def get_suggested_amount(self):
        return self.suggested_amount

    def __str__(self):
        result = ""
