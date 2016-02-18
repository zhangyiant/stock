import logging

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, Integer, String, Float, Date
from sqlalchemy.orm import make_transient
from sqlalchemy.orm import relationship

from stock_db.db_connection import StockDbConnection
from stock_db.db_connection import get_default_db_connection
from sqlalchemy.orm.session import make_transient
import sqlalchemy

Base = declarative_base()

class StockInfo(Base):
    
    __tablename__ = 'stock_info'
    
    symbol = Column(String(20), primary_key=True)
    name = Column(String(20))
    
    stock_cash = relationship("StockCash", uselist = False, backref="stock_info")
    stock_transactions = relationship("StockTransaction", order_by="StockTransaction.trans_id", backref="stock_info")
    
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
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        session.add(stock_info)
        
        session.commit()
        
        session.refresh(stock_info)
        
        make_transient(stock_info)
        
        session.close()
        
        return stock_info

    def get_all_stock_info(self):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        stock_info_list = session.query(StockInfo).all()
        
        new_stock_info_list = []
        for stock_info in stock_info_list:
            make_transient(stock_info)
            new_stock_info_list.append(stock_info)
        session.close()
        return new_stock_info_list

    def get_stock_info_by_symbol(self, symbol):
        Session = self.conn.get_sessionmake()
        session = Session()
        stock_info = session.query(StockInfo).filter(StockInfo.symbol==symbol).scalar()
        if stock_info is not None:
            make_transient(stock_info)
        session.close()
        return stock_info

    def update_stock_info(self, stock_info):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        new_stock_info = session.merge(stock_info)
        
        session.commit()
        
        session.refresh(new_stock_info)
        
        make_transient(new_stock_info)
        
        session.close()
        
        return new_stock_info

    def delete_stock_info(self, stock_info):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        new_stock_info = session.merge(stock_info)
        
        session.delete(new_stock_info)
        
        session.commit()
        
        session.close()
        
        return


class StockCash(Base):
    
    __tablename__ = "stock_cash"
    
    symbol = Column(String(20), ForeignKey("stock_info.symbol"),  primary_key=True)
    amount = Column(Float)
    
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
        Session = self.conn.get_sessionmake()
        session = Session()
        
        session.add(stock_cash)
        
        session.commit()

        session.refresh(stock_cash)
        
        make_transient(stock_cash)
        
        session.close()
        
        return stock_cash

    def get_all_stock_cash(self):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        query_stock_cash_list = session.query(StockCash).all()
        stock_cash_list = []
        for stock_cash in query_stock_cash_list:
            make_transient(stock_cash)
            stock_cash_list.append(stock_cash)
            
        session.close()
        
        return stock_cash_list

    def get_stock_cash_by_symbol(self, symbol):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        stock_cash = session.query(StockCash).filter(StockCash.symbol==symbol).scalar()
        if stock_cash is not None:
            make_transient(stock_cash)
            
        session.close()
        return stock_cash

    def update_stock_cash(self, stock_cash):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        new_stock_cash = session.merge(stock_cash)
        
        session.commit()
        
        session.refresh(new_stock_cash)
        
        make_transient(new_stock_cash)
                       
        session.close()
        
        return new_stock_cash

    def delete_stock_cash(self, stock_cash):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        new_stock_cash = session.merge(stock_cash)
        
        session.delete(new_stock_cash)
        
        session.commit()
        
        session.close()
        
        return

class StockTransaction(Base):
    
    __tablename__ = "stock_transaction"
    
    trans_id = Column(Integer, primary_key=True)
    symbol = Column(String(20), ForeignKey("stock_info.symbol"))
    buy_or_sell = Column(String(20))
    quantity = Column(Integer)
    price = Column(Float)
    date = Column(Date)
    
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
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        session.add(stock_transaction)
        session.commit()
        
        session.refresh(stock_transaction)
        make_transient(stock_transaction)
        
        session.close()
        return stock_transaction

    def get_all_stock_transaction(self):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        query_stock_transaction_list = session.query(StockTransaction).all()
        
        stock_transaction_list = []
        for stock_transaction in query_stock_transaction_list:
            make_transient(stock_transaction)
            stock_transaction_list.append(stock_transaction)
            
        session.close()
        return stock_transaction_list

    # below is not updated yet.
    def get_stock_transaction_by_trans_id(self, trans_id):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        stock_transaction = session.query(StockTransaction).filter(StockTransaction.trans_id == trans_id).scalar()
        
        if stock_transaction is not None:
            make_transient(stock_transaction)
        session.close()
        
        return stock_transaction

    def get_stock_transaction_list_by_symbol(self, symbol):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        query_stock_transaction_list = session.query(StockTransaction).filter(StockTransaction.symbol == symbol).all()

        stock_transaction_list = []
        for stock_transaction in query_stock_transaction_list:
            make_transient(stock_transaction)
            stock_transaction_list.append(stock_transaction)

        session.close()

        return stock_transaction_list

    def update_stock_transaction(self, stock_transaction):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        new_stock_transaction = session.merge(stock_transaction)
        session.commit()
        
        session.refresh(new_stock_transaction)
        make_transient(new_stock_transaction)
        
        session.close()
        
        return new_stock_transaction


    def delete_stock_transaction(self, stock_transaction):
        
        Session = self.conn.get_sessionmake()
        session = Session()
        
        new_stock_transaction =  session.merge(stock_transaction)
        
        session.delete(new_stock_transaction)
        
        session.commit()
        
        return

class StockPriceRange(Base):
    
    __tablename__ = "stock_price_range"
    
    symbol = Column(String(20), ForeignKey("stock_info.symbol"),  primary_key=True)
    price_low = Column(Float)
    price_high = Column(Float)
    
    def __init__(self, symbol=None, price_low=None, price_high=None):
        self.symbol = symbol
        self.price_low = price_low
        self.price_high = price_high
        return

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def get_price_low(self):
        return self.price_low

    def set_price_low(self, price):
        self.price_low = price
        return

    def get_price_high(self):
        return self.price_high
    
    def set_price_high(self, price):
        self.price_high = price
        return
    
    def __str__(self):
        result = "Symbol:{0}\t Price_low:{1}\t Price_high:{2}".format(self.symbol, self.price_low, self.price_high)
        return result
    
class StockPriceRangeTable:
    def __init__(self, conn = None):
        if (conn is None):
            conn = get_default_db_connection()
        self.logger = logging.getLogger(__name__ + ".StockPriceRangeTable")
        self.conn = conn
        return

    def add_stock_price_range(self, stock_price_range):
        Session = self.conn.get_sessionmake()
        session = Session()
        
        session.add(stock_price_range)
        
        session.commit()

        session.refresh(stock_price_range)
        
        make_transient(stock_price_range)
        
        session.close()
        
        return stock_price_range

    def get_all_stock_price_range(self):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        query_stock_price_range_list = session.query(StockPriceRange).all()
        stock_price_range_list = []
        for stock_price_range in query_stock_price_range_list:
            make_transient(stock_price_range)
            stock_price_range_list.append(stock_price_range)
            
        session.close()
        
        return stock_price_range_list

    def get_stock_stock_price_range_by_symbol(self, symbol):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        stock_price_range = session.query(StockPriceRange).filter(StockPriceRange.symbol==symbol).scalar()
        if stock_price_range is not None:
            make_transient(stock_price_range)
            
        session.close()
        return stock_price_range

    def update_stock_price_range(self, stock_price_range):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        new_stock_price_range = session.merge(stock_price_range)
        
        session.commit()
        
        session.refresh(new_stock_price_range)
        
        make_transient(new_stock_price_range)
                       
        session.close()
        
        return new_stock_price_range

    def delete_stock_price_range(self, stock_price_range):
        
        Session = self.conn.get_sessionmake()
        
        session = Session()
        
        new_stock_price_range = session.merge(stock_price_range)
        
        session.delete(new_stock_price_range)
        
        session.commit()
        
        session.close()

        return