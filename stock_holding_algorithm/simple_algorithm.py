from stock_db.db_stock import StockCashTable, StockCash
from stock_db.db_stock import StockTransactionTable, StockTransaction
from stock_db.db_connection import get_default_db_connection

class SimpleAlgorithm:
    def __init__(self, symbol = None, start_price = None, stop_price = None,
                 current_price = None, conn = None):
        if conn == None:
            self.conn = get_default_db_connection()
        else:
            self.conn = conn
        self.symbol = symbol
        self.start_price = start_price
        self.stop_price = stop_price
        self.current_price = current_price
        self.suggested_buy_or_sell = None
        self.suggested_amount = 0

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol
        return

    def get_start_price(self):
        return self.start_price

    def get_stop_price(self):
        return self.stop_price

    def get_current_price(self):
        return self.current_price

    def get_connection(self):
        return self.conn

    def set_start_price(self, start_price):
        self.start_price = start_price
        return

    def set_stop_price(self, stop_price):
        self.stop_price = stop_price
        return

    def set_current_price(self, current_price):
        self.current_price = current_price
        return

    def set_connection(self, conn):
        self.conn = conn
        return

    def get_expected_percentage(self):
        current_price_percentage = (self.current_price - self.start_price) / \
                                   (self.stop_price - self.start_price)
        if (current_price_percentage >= 0 ) and \
           (current_price_percentage < 0.25):
            expected_percentage = \
                ((0.25 - current_price_percentage) / 0.25 * 0.5 + 0.5) * 100
        elif (current_price_percentage >= 0.25) and \
             (current_price_percentage < 0.5):
            expected_percentage = \
                ((0.5 - current_price_percentage) / 0.25 * 0.25 + 0.25) * 100
        elif (current_price_percentage >= 0.5) and \
            (current_price_percentage < 0.75):
            expected_percentage = \
                ((0.75 - current_price_percentage) / 0.25 * 0.125 + 0.125) * 100
        elif (current_price_percentage >= 0.75) and \
            (current_price_percentage <= 1):
            expected_percentage = \
                ((1 - current_price_percentage) / 0.25 * 0.125) * 100
        else:
            expected_percentage = None
        return expected_percentage

    def get_total_value(self):
        current_cash = self.get_cash_value()
        stock_value = self.get_stock_value()
        total = current_cash + stock_value
        return total

    def get_cash_value(self):
        stock_cash_table = StockCashTable(self.conn)
        stock_cash = stock_cash_table.get_stock_cash_by_symbol(self.symbol)
        amount = stock_cash.get_amount()
        return amount

    def get_stock_quantity(self):
        stock_transaction_table = StockTransactionTable(self.conn)
        stock_transaction_list = \
            stock_transaction_table.get_stock_transaction_list_by_symbol(\
                self.symbol)
        quantity = 0
        for stock_transaction in stock_transaction_list:
            buy_or_sell = stock_transaction.get_buy_or_sell()
            if (buy_or_sell == "Buy"):
                quantity = quantity + stock_transaction.get_quantity()
            elif (buy_or_sell == "Sell"):
                quantity = quantity - stock_transaction.get_quantity()
            else:
                # Need to raise an error
                return None
        return quantity

    def get_stock_value(self):
        stock_value = self.get_stock_quantity() * self.current_price
        return stock_value

    def get_current_percentage(self):
        current_cash = self.get_cash_value()
        stock_value = self.get_stock_value()
        current_percentage = stock_value / (current_cash + stock_value) * 100
        return current_percentage

    def calculate(self):
        expected_percentage = self.get_expected_percentage()
        current_percentage = self.get_current_percentage()
        if (current_percentage > expected_percentage):
            self.suggested_buy_or_sell = "Sell"
            diff_percentage = current_percentage - expected_percentage
            diff_value = diff_percentage / 100 * self.get_total_value()
            self.suggested_amount = diff_value / self.current_price
        else:
            self.suggested_buy_or_sell = "Buy"
            diff_percentage = expected_percentage - current_percentage
            diff_value = diff_percentage / 100 * self.get_total_value()
            self.suggested_amount = diff_value / self.current_price
        return

    def get_suggested_buy_or_sell(self):
        return self.suggested_buy_or_sell

    def get_suggested_amount(self):
        return self.suggested_amount

    def __str__(self):
        result = ""
