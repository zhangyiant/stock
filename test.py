import logging
import unittest
from stock_holding_algorithm.simple_algorithm import SimpleAlgorithm
from stock_db.db_connection import StockDbConnection
from stock_db.db_stock import StockCashTable
from stock_db.db_stock import StockCash
from stock_db.db_stock import StockTransaction
from stock_db.db_stock import StockTransactionTable

class StockDbConnectionTest(unittest.TestCase):
    def setUp(self):
        return

    def test_simple_algorithm(self):
        a = SimpleAlgorithm(3,4)
        percentage = a.get_percentage(5)
        self.assertEqual(percentage, 100)

    def test_db_connection(self):
        stock_db_connection = StockDbConnection("example.db")
        conn = stock_db_connection.connect()
        cursor = stock_db_connection.get_cursor()

        cursor.execute("drop table if exists test_db_connection")
        conn.commit()

        cursor.execute("create table test_db_connection(id, age)")
        cursor.execute("insert into test_db_connection values (?,?)", (2,50))
        conn.commit()
        cursor.execute("select * from test_db_connection")
        self.assertEqual(cursor.fetchall(), [(2,50)])
        stock_db_connection.close()

    def test_reset_table(self):
        # test
        logging.info("new StockDbConnection")
        stock_db_connection = StockDbConnection("example.db")
        logging.info("reset table")
        stock_db_connection.reset_table()
        conn = stock_db_connection.get_connection()
        cursor = stock_db_connection.get_cursor()

        cursor.execute("select * from stock_cash")
        data = cursor.fetchall()
        self.assertEqual(data, [])

        cursor.execute("select * from stock_transaction")
        data = cursor.fetchall()
        self.assertEqual(data, [])

        logging.info("close connection")
        stock_db_connection.close()

    def test_insert_table_data(self):
        stock_db_connection = StockDbConnection("example.db")
        stock_db_connection.reset_table()
        conn = stock_db_connection.connect()
        cursor = stock_db_connection.get_cursor()

        cursor.execute("insert into stock_cash values (?,?)", ("601398", 1500.001))
        cursor.execute("insert into stock_cash values (?,?)", ("601390", 1234567890.789))

        cursor.execute("insert into stock_transaction(symbol, buy_or_sell, quantity, price, date) values(?,?,?,?,?)", ("601398", "buy", 200, 5.56, "2015-1-4"))
        cursor.execute("insert into stock_transaction(symbol, buy_or_sell, quantity, price, date) values(?,?,?,?,?)", ("601390", "sell", 1500, 8.12, "2015-5-6"))

        conn.commit()

        cursor.execute("select * from stock_cash")
        data = cursor.fetchall()
        self.assertEqual(data, [('601398', 1500.001),('601390', 1234567890.789)])
        cursor.execute("select * from stock_transaction")
        data = cursor.fetchall()
        self.assertEqual(data,
                         [(1, "601398", "buy", 200, 5.56, "2015-1-4"),
                          (2, "601390", "sell", 1500, 8.12, "2015-5-6")])

    def test_stock_cash_sanity(self):
        stock_db_connection = StockDbConnection("example.db")
        stock_db_connection.reset_table()
        stock_cash_table = StockCashTable(stock_db_connection)
        stock_cash = StockCash("601398", 1000)
        stock_cash_table.add_stock_cash(stock_cash)

        # test the new created line
        stock_cash = stock_cash_table.get_stock_cash_by_symbol("601398")
        self.assertEqual(stock_cash.get_symbol(), "601398")
        self.assertEqual(stock_cash.get_amount(), 1000)

        # test update stock cash
        stock_cash.set_amount(123456.566)
        stock_cash_table.update_stock_cash(stock_cash)
        stock_cash = stock_cash_table.get_stock_cash_by_symbol("601398")
        self.assertEqual(stock_cash.get_amount(), 123456.566)

        # test an unavailable line
        stock_cash = stock_cash_table.get_stock_cash_by_symbol("601390")
        self.assertEqual(stock_cash, None)

        # insert a new line, and test get_all function
        stock_cash = StockCash("601390", 5000)
        stock_cash_table.add_stock_cash(stock_cash)
        stock_cash_list = stock_cash_table.get_all_stock_cash()
        self.assertEqual(len(stock_cash_list), 2)
        stock_cash = stock_cash_list[0]
        self.assertEqual(stock_cash.get_symbol(), "601398")
        self.assertEqual(stock_cash.get_amount(), 123456.566)
        stock_cash = stock_cash_list[1]
        self.assertEqual(stock_cash.get_symbol(), "601390")
        self.assertEqual(stock_cash.get_amount(), 5000)

        # delete a line
        stock_cash = StockCash("601398", 0)
        stock_cash_table.delete_stock_cash(stock_cash)
        stock_cash = stock_cash_table.get_stock_cash_by_symbol("601398")
        self.assertEqual(stock_cash, None)

    def test_stock_transaction_sanity(self):
        stock_db_connection = StockDbConnection("example.db")
        stock_db_connection.reset_table()
        stock_transaction_table = StockTransactionTable(stock_db_connection)
        stock_transaction = StockTransaction()
        stock_transaction.set_symbol("601398")
        stock_transaction.set_buy_or_sell("buy")
        stock_transaction.set_quantity(100)
        stock_transaction.set_price(4.51)
        stock_transaction.set_date("2015-5-20")
        stock_transaction_table.add_stock_transaction(stock_transaction)

        stock_transaction.set_symbol("601855")
        stock_transaction_table.add_stock_transaction(stock_transaction)

        stock_transaction_list = \
            stock_transaction_table.get_all_stock_transaction()
        print("new table\n")
        for stock_transaction in stock_transaction_list:
            print("{0}".format(stock_transaction) + "\n")

        stock_transaction = \
            stock_transaction_table.get_stock_transaction_by_trans_id(1)
        stock_transaction.set_symbol("xxxxxx")
        stock_transaction_table.update_stock_transaction(stock_transaction)

        print("new table\n")
        stock_transaction_list = \
            stock_transaction_table.get_all_stock_transaction()
        for stock_transaction in stock_transaction_list:
            print("{0}".format(stock_transaction) + "\n")

        stock_transaction = \
            stock_transaction_table.get_stock_transaction_by_trans_id(1)
        stock_transaction_table.delete_stock_transaction(stock_transaction)

        print("new table\n")
        stock_transaction_list = \
            stock_transaction_table.get_all_stock_transaction()
        for stock_transaction in stock_transaction_list:
            print("{0}".format(stock_transaction) + "\n")

        return

def main():
    logging.basicConfig(filename="test.log", level=logging.DEBUG)
    logging.info("Started")
    unittest.main()

if __name__ == "__main__":
    main()
