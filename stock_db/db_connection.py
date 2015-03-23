import logging
import sqlite3

class StockDbConnection:
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__ + ".StockDbConnection")
        self.filename = filename
        self.conn = None

    def connect(self):
        if self.is_connected():
            return self.conn
        self.conn = sqlite3.connect(self.filename)
        return self.conn

    def close(self):
        if self.is_connected():
            self.conn.close()

    def is_connected(self):
        if self.conn != None:
            return True
        else:
            return False

    def get_connection(self):
        return self.conn

    def get_cursor(self):
        if self.is_connected():
            return self.conn.cursor()
        else:
            return None

    def reset_table(self):
        if not self.is_connected():
            self.connect()
        conn = self.get_connection()

        # drop table
        self.logger.info("drop table")
        cursor = self.get_cursor()
        cursor.execute("drop table if exists stock_cash")
        cursor.execute("drop table if exists stock_transaction")
        conn.commit()

        # create table
        self.logger.info("create table")
        cursor.execute('''create table stock_cash (
                              symbol text primary key,
                              amount real)''')
        cursor.execute('''create table stock_transaction(
                              id integer primary key,
                              symbol text,
                              trans  text,
                              quantity integer,
                              price real,
                              date text)''')
        conn.commit()
 
    def display_table_data(self):
        conn = self.connect()
        cursor = self.get_cursor()
       
        print("Cash Table:") 
        cursor.execute("select * from stock_cash")
        print(cursor.fetchall())

        print("Transaction Table:")
        cursor.execute("select * from stock_transaction")
        print(cursor.fetchall())

DB_CONN = None

def get_default_db_connection():
    global DB_CONN
    if (DB_CONN is None):
        DB_CONN = StockDbConnection("stock.db")

    return DB_CONN
