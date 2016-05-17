'''
    db_utility module
'''
import logging
import csv

from stock_db.db_connection import get_default_db_connection
from stock_db.db_stock import StockInfoTable, StockInfo
import stock_db.db_stock

LOGGER = logging.getLogger(__name__ + ".StockDbUtility")

def import_stock_info(conn=None):
    '''
        import_stock_info
    '''
    if conn is None:
        stock_info_table = StockInfoTable()
    else:
        stock_info_table = StockInfoTable(conn)

    with open("stock_info.csv", newline="", encoding="utf-8") as file_handler:
        reader = csv.reader(file_handler)
        for row in reader:
            stock_symbol = row[0]
            stock_name = row[1]
            stock_info = \
                stock_info_table.get_stock_info_by_symbol(stock_symbol)
            if stock_info != None:
                stock_info = \
                    StockInfo(stock_symbol, stock_name)
                stock_info_table.update_stock_info(stock_info)
            else:
                stock_info = \
                    StockInfo(stock_symbol, stock_name)
                stock_info_table.add_stock_info(stock_info)
    return

def reset_table(conn = None):
    '''
        reset_table
    '''
    if conn is None:
        db_connection = get_default_db_connection()
    else:
        db_connection = conn

    base = stock_db.db_stock.Base

    engine = db_connection.get_engine()

    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)

    # import stock info from csv file
    import_stock_info()

    return

def recreate_db(conn=None):
    '''
        recreate_db
    '''
    if conn is None:
        db_connection = get_default_db_connection()
    else:
        db_connection = conn

    base = stock_db.db_stock.Base

    engine = db_connection.get_engine()

    base.metadata.create_all(engine)

    return


if __name__ == "__main__":
    recreate_db()
