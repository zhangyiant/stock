import logging
import sqlite3
import csv

class StockDbConnection:
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__ + ".StockDbConnection")b
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
