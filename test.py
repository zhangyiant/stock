import logging
import unittest
from stock_holding_algorithm.simple_algorithm import simple_algorithm
from stock_db.db_connection import StockDbConnection

class StockDbConnectionTest(unittest.TestCase):
    def setUp(self):
        return

    def test_simple_algorithm(self):
        a = simple_algorithm(3,4)
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

        cursor.execute("insert into stock_transaction(symbol, trans, quantity, price, date) values(?,?,?,?,?)", ("601398", "buy", 200, 5.56, "2015-1-4"))
        cursor.execute("insert into stock_transaction(symbol, trans, quantity, price, date) values(?,?,?,?,?)", ("601390", "sell", 1500, 8.12, "2015-5-6"))

        conn.commit()

        cursor.execute("select * from stock_cash")
        data = cursor.fetchall()
        self.assertEqual(data, [('601398', 1500.001),('601390', 1234567890.789)])
        cursor.execute("select * from stock_transaction")
        data = cursor.fetchall()
        self.assertEqual(data, 
                         [(1, "601398", "buy", 200, 5.56, "2015-1-4"), 
                          (2, "601390", "sell", 1500, 8.12, "2015-5-6")])

def main():
    logging.basicConfig(filename="test.log", level=logging.DEBUG) 
    logging.info("Started") 
    unittest.main()
 
if __name__ == "__main__":
    main()

