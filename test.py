from stock_holding_algorithm.simple_algorithm import simple_algorithm
from stock_db.db_connection import StockDbConnection

def test_simple_algorithm():
    a = simple_algorithm(3,4)
    print(a.get_percentage(5))

def test_db_connection():
    stock_db_connection = StockDbConnection("example.db")
    conn = stock_db_connection.connect()
    cursor = stock_db_connection.get_cursor()

    #cursor.execute("create table test_db_connection(id, age)")
    cursor.execute("insert into test_db_connection values (?,?)", (2,50))
    conn.commit()
    cursor.execute("select * from test_db_connection")
    print(cursor.fetchall()) 
    stock_db_connection.close()


test_db_connection()



