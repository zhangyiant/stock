import sqlite3

class StockDbConnection:
    def __init__(self, filename):
        self.filename = filename
        self.conn = None

    def connect(self):
        self.conn = sqlite3.connect(self.filename)
        return self.conn

    def close(self):
        self.conn.close()

    def is_connected(self):
        if self.conn != None:
            return True
        else:
            return False

    def get_cursor(self):
        if self.is_connected():
            return self.conn.cursor()
        else:
            return None

        

