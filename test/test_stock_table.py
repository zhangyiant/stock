import logging
import unittest
import configparser
import stock_db
from stock_db.db_stock import StockClosedTransaction
from stock_db.db_stock import StockClosedTransactionTable
from stock_db.db_utility import reset_table
from stock_db.db_connection import get_default_db_connection
from datetime import date

class StockClosedTransactionTableTest(unittest.TestCase):
    def setUp(self):
        config = configparser.ConfigParser()
        config.read("stock.ini", encoding="utf-8")
        connection_string = config['Database'].get('test_connection')
        stock_db.db_connection.default_connection_string = connection_string
        return

    def test_stock_closed_transaction_sanity(self):
        stock_db_connection = get_default_db_connection()
        reset_table(stock_db_connection)
        transaction_table = StockClosedTransactionTable(stock_db_connection)
        # new a stock closed transaction
        stock_closed_transaction = StockClosedTransaction()
        stock_closed_transaction.symbol = "601398"
        stock_closed_transaction.buy_price = 4.51
        stock_closed_transaction.sell_price = 4.61
        stock_closed_transaction.buy_date = date(2015, 11, 10)
        stock_closed_transaction.sell_date = date(2015, 12, 30)
        stock_closed_transaction.quantity = 200
        transaction_table.add_stock_closed_transaction(
                                                  stock_closed_transaction)

        # query and compare
        stock_closed_transaction_list = \
                transaction_table.get_all_stock_closed_transaction()
        self.assertEqual(len(stock_closed_transaction_list),
                         1,
                         "There should be only 1 item")
        stock_closed_transaction = stock_closed_transaction_list[0]
        self.assertEqual(stock_closed_transaction.symbol,
                         "601398")
        self.assertEqual(stock_closed_transaction.buy_price,
                         4.51)
        self.assertEqual(stock_closed_transaction.sell_price,
                         4.61)
        self.assertEqual(stock_closed_transaction.buy_date,
                         date(2015, 11, 10))
        self.assertEqual(stock_closed_transaction.sell_date,
                         date(2015, 12, 30))
        self.assertEqual(stock_closed_transaction.quantity,
                         200)

        # delete the newly created item
        transaction_table.delete_stock_closed_transaction(
            stock_closed_transaction)
        stock_closed_transaction_list = \
                transaction_table.get_all_stock_closed_transaction()
        self.assertEqual(len(stock_closed_transaction_list),
                         0,
                         "The list should be an empty list")

        return
