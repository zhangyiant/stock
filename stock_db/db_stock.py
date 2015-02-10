import logging
from stock_db.db_connection import StockDbConnection

class StockCash:
    def __init__(self, symbol=None, amount=None):
        self.symbol = symbol
        self.amount = amount

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def get_amount(self):
        return self.amount

    def set_amount(self):
        return self.amount
   
class StockCashTable:
    def __init__(self, conn):
        self.logger = logging.getLogger(__name__ + ".StockCashTable")
        self.conn = conn
        return

    def add_stock_cash(self, stock_cash):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_cash.get_symbol()
        amount = stock_cash.get_amount()
        cursor.execute("insert into stock_cash values(?,?)",(symbol, amount))
        conn.commit()


    def get_stock_cash_by_symbol(self, symbol):
        return
