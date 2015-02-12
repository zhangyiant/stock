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

    def set_amount(self, amount):
        self.amount = amount
        return
   
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

        stock_cash = StockCash(symbol, amount)

        return stock_cash 


    def get_stock_cash_by_symbol(self, symbol):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        cursor.execute("select * from stock_cash where symbol=?", (symbol,))
        result = cursor.fetchone()
        if result == None:
            return None
        symbol = result[0]
        amount = result[1]
        stock_cash = StockCash(symbol, amount) 
        return stock_cash

    def update_stock_cash(self, stock_cash):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_cash.get_symbol()
        amount = stock_cash.get_amount()

        self.logger.debug("update stock_cash, symbol=%s, amount=%d", 
                      symbol, amount)
        cursor.execute("update stock_cash set amount=? where symbol=?", 
                       (amount, symbol))
        conn.commit()
        return

        
