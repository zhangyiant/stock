import logging
from stock_db.db_connection import StockDbConnection
from stock_db.db_connection import get_default_db_connection

class StockInfo:
    def __init__(self, symbol = None, name = None):
        self.symbol = symbol
        self.name = name

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        return

    def __str__(self):
        result = "Symbol:{0}\t Name:{1}".format(self.symbol, self.name)
        return result

class StockInfoTable:
    def __init__(self, conn = None):
        if (conn is None):
            conn = get_default_db_connection()
        self.logger = logging.getLogger(__name__ + ".StockInfoTable")
        self.conn = conn
        return

    def add_stock_info(self, stock_info):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_info.get_symbol()
        name = stock_info.get_name()
        cursor.execute("insert into stock_info values(?,?)",(symbol, name))
        conn.commit()

        stock_info = StockInfo(symbol, name)

        return stock_info

    def get_all_stock_info(self):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        cursor.execute("select * from stock_info")
        result = cursor.fetchall()
        stock_info_list = []
        for elem in result:
            symbol = elem[0]
            name = elem[1]
            stock_info = StockInfo(symbol, name)
            stock_info_list.append(stock_info)
        return stock_info_list

    def get_stock_info_by_symbol(self, symbol):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        cursor.execute("select * from stock_info where symbol=?", (symbol,))
        result = cursor.fetchone()
        if result == None:
            return None
        symbol = result[0]
        name = result[1]
        stock_info = StockCash(symbol, name)
        return stock_info

    def update_stock_info(self, stock_info):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_info.get_symbol()
        name = stock_info.get_name()

        self.logger.debug("update stock_info, symbol=%s, name=%d",
                          symbol, name)
        cursor.execute("update stock_info set name=? where symbol=?",
                       (name, symbol))
        conn.commit()
        return

    def delete_stock_info(self, stock_info):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_cash.get_symbol()

        cursor.execute("delete from stock_info where symbol=?", (symbol,))

        conn.commit()
        return

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

    def __str__(self):
        result = "Symbol:{0}\t Amount:{1}".format(self.symbol, self.amount)
        return result

class StockCashTable:
    def __init__(self, conn = None):
        if (conn is None):
            conn = get_default_db_connection()
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

    def get_all_stock_cash(self):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        cursor.execute("select * from stock_cash")
        result = cursor.fetchall()
        stock_cash_list = []
        for elem in result:
            symbol = elem[0]
            amount = elem[1]
            stock_cash = StockCash(symbol, amount)
            stock_cash_list.append(stock_cash)
        return stock_cash_list

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

    def delete_stock_cash(self, stock_cash):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_cash.get_symbol()

        cursor.execute("delete from stock_cash where symbol=?", (symbol,))

        conn.commit()
        return

class StockTransaction:
    def __init__(self, trans_id = None):
        self.trans_id = trans_id
        self.symbol = None
        self.buy_or_sell = None
        self.quantity = None
        self.price = None
        self.date = None
        return

    def get_trans_id(self):
        return self.trans_id

    def set_trans_id(self, trans_id):
        self.trans_id = trans_id
        return
    
    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def get_buy_or_sell(self):
        return self.buy_or_sell

    def set_buy_or_sell(self, buy_or_sell):
        self.buy_or_sell = buy_or_sell
        return

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        return

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price
        return

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date
        return

    def __str__(self):
        result = "Trans ID: {0}\tSymbol: {1}".format(self.trans_id, self.symbol)
        result = result + "\t{0}\tquantity: {1}\tprice: {2}".format(
            self.buy_or_sell, self.quantity, self.price)
        result = result + "\tDate: {0}".format(self.date)
        return result

class StockTransactionTable:
    def __init__(self, conn = None):
        if (conn is None):
            conn = get_default_db_connection()
        self.logger = logging.getLogger(__name__ + ".StockTransactionTable")
        self.conn = conn
        return

    def add_stock_transaction(self, stock_transaction):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        symbol = stock_transaction.get_symbol()
        buy_or_sell = stock_transaction.get_buy_or_sell()
        quantity = stock_transaction.get_quantity()
        price = stock_transaction.get_price()
        date = stock_transaction.get_date()
        cursor.execute('''insert into stock_transaction(symbol,
                                                      buy_or_sell,
                                                      quantity,
                                                      price,
                                                      date)
                                           values(?,?,?,?,?)''',
                       (symbol, buy_or_sell, quantity, price, date))
        conn.commit()

        stock_transaction = StockTransaction()

        return stock_transaction

    def get_all_stock_transaction(self):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        cursor.execute("select * from stock_transaction")
        result = cursor.fetchall()
        stock_transaction_list = []
        for elem in result:
            trans_id = elem[0]
            symbol = elem[1]
            buy_or_sell = elem[2]
            quantity = elem[3]
            price = elem[4]
            date = elem[5]
            stock_transaction = StockTransaction()
            stock_transaction.set_trans_id(trans_id)
            stock_transaction.set_symbol(symbol)
            stock_transaction.set_buy_or_sell(buy_or_sell)
            stock_transaction.set_quantity(quantity)
            stock_transaction.set_price(price)
            stock_transaction.set_date(date)
            stock_transaction_list.append(stock_transaction)
        return stock_transaction_list

    # below is not updated yet.
    def get_stock_transaction_by_trans_id(self, trans_id):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        cursor.execute("select * from stock_transaction where trans_id=?", \
                       (trans_id,))
        result = cursor.fetchone()
        if result == None:
            return None
        stock_transaction = StockTransaction()
        stock_transaction.set_trans_id(result[0])
        stock_transaction.set_symbol(result[1])
        stock_transaction.set_buy_or_sell(result[2])
        stock_transaction.set_quantity(result[3])
        stock_transaction.set_price(result[4])
        stock_transaction.set_date(result[5])
        return stock_transaction

    def update_stock_transaction(self, stock_transaction):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        trans_id = stock_transaction.get_trans_id()
        symbol = stock_transaction.get_symbol()
        buy_or_sell = stock_transaction.get_buy_or_sell()
        quantity = stock_transaction.get_quantity()
        price = stock_transaction.get_price()
        date = stock_transaction.get_date()

        self.logger.debug("update stock_transaction, symbol=%s, price=%d", 
                          symbol, price)
        cursor.execute('''update stock_transaction set symbol=?, 
                                                       buy_or_sell=?,
                                                       quantity=?,
                                                       price=?,
                                                       date=? 
                                                   where trans_id=?''', 
                       (symbol, buy_or_sell, quantity, price, date, trans_id))
        conn.commit()
        return

    def delete_stock_transaction(self, stock_transaction):
        conn = self.conn.connect()
        cursor = self.conn.get_cursor()
        trans_id = stock_transaction.get_trans_id()

        cursor.execute("delete from stock_transaction where trans_id=?",
                       (trans_id,))

        conn.commit()
        return
