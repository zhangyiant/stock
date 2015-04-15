import logging
import csv
from stock_db.db_connection import StockDbConnection
from stock_db.db_connection import get_default_db_connection
from stock_db.db_stock import StockInfoTable, StockInfo

logger = logging.getLogger(__name__ + ".StockDbUtility")

def import_stock_info():
    db_connection = get_default_db_connection()
    conn = db_connection.connect()
    cursor = db_connection.get_cursor()

    stock_info_table = StockInfoTable()
    with open("stock_info.csv", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            stock_symbol = row[0]
            stock_name = row[1]
            stock_info = \
                StockInfo(stock_symbol, stock_name)
            stock_info_table.add_stock_info(stock_info)
    return

def reset_table():
    db_connection = get_default_db_connection()
    conn = db_connection.connect()

    # drop table
    logger.info("drop table")
    cursor = db_connection.get_cursor()
    cursor.execute("drop table if exists stock_info")
    cursor.execute("drop table if exists stock_cash")
    cursor.execute("drop table if exists stock_transaction")
    conn.commit()

    # create table
    logger.info("create table")
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

    # import stock info from csv file
    import_stock_info()

    return
