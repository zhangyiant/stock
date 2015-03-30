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
        self.turn_on_foreign_key()
        return self.conn

    def turn_on_foreign_key(self):
        cur = self.get_cursor()
        cur.execute("PRAGMA foreign_keys = ON")
        self.conn.commit()
        cur.execute("PRAGMA foreign_keys")
        print(cur.fetchone())
        return

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
        cursor.execute("drop table if exists stock_info")
        conn.commit()

        # create table
        self.logger.info("create table")
        cursor.execute('''create table stock_info (
                              symbol text primary key,
                              name text)''')
        cursor.execute('''create table stock_cash (
                              symbol text primary key,
                              amount real,
                              FOREIGN KEY(symbol) REFERENCES stock_info(symbol)
                              )''')
        cursor.execute('''create table stock_transaction(
                              trans_id integer primary key,
                              symbol text,
                              buy_or_sell  text,
                              quantity integer,
                              price real,
                              date text,
                              FOREIGN KEY(symbol) REFERENCES stock_info(symbol)
                              )''')
        conn.commit()

        self.import_stock_info()
        return

    def import_stock_info(self):
        if not self.is_connected():
            self.connect()
        conn = self.get_connection()

        cursor = self.get_cursor()
        cursor.execute('''insert into stock_info (symbol, name)
                              values(?,?)''',
                       ("601398", "工商银行"))
        cursor.execute('''insert into stock_info (symbol, name)
                              values(?,?)''',
                       ("601857", "中国石油"))
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
