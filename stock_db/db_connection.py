import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class StockDbConnection:
    def __init__(self, filename):
        self.logger = logging.getLogger(__name__ + ".StockDbConnection")
        self.filename = filename
#        self.engine = create_engine('sqlite:///%s' % filename)
        self.engine = create_engine('mysql+mysqlconnector://root:anteestudio@192.168.1.235/my_test_db?charset=utf8mb4')
        self.Session = sessionmaker(bind=self.engine)
        self.conn = None
        return
    
    def get_engine(self):
        return self.engine
    
    def get_sessionmake(self):
        return self.Session  
    
DB_CONN = None

def get_default_db_connection():
    global DB_CONN
    if (DB_CONN is None):
        DB_CONN = StockDbConnection("stock.db")

    return DB_CONN

