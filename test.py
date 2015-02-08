from stock_holding_algorithm.simple_algorithm import simple_algorithm
from stock_db.db_connection import StockDbConnection

def test_simple_algorithm():
    a = simple_algorithm(3,4)
    print(a.get_percentage(5))

def test_db_connection():
    stock_db_connection = StockDbConnection("example.db")
    conn = stock_db_connection.connect()
    cursor = stock_db_connection.get_cursor()

    cursor.execute("drop table if exists test_db_connection")
    conn.commit()

    cursor.execute("create table test_db_connection(id, age)")
    cursor.execute("insert into test_db_connection values (?,?)", (2,50))
    conn.commit()
    cursor.execute("select * from test_db_connection")
    print(cursor.fetchall()) 
    stock_db_connection.close()

def test_reset_table():
    stock_db_connection = StockDbConnection("example.db")
    stock_db_connection.reset_table()
    stock_db_connection.display_table_data()
    stock_db_connection.close()

def test_insert_table_data():
    stock_db_connection = StockDbConnection("example.db")
    conn = stock_db_connection.connect()
    cursor = stock_db_connection.get_cursor()

    cursor.execute("insert into stock_cash values (?,?)", ("601398", 1500.001))
    cursor.execute("insert into stock_cash values (?,?)", ("601390", 1234567890.789))

    cursor.execute("insert into stock_transaction(symbol, trans, quantity, price, date) values(?,?,?,?,?)", ("601398", "buy", 200, 5.56, "2015-1-4"))
    cursor.execute("insert into stock_transaction(symbol, trans, quantity, price, date) values(?,?,?,?,?)", ("601390", "sell", 1500, 8.12, "2015-5-6"))

    conn.commit()

    stock_db_connection.display_table_data()

test_db_connection()
test_reset_table()
test_insert_table_data()


