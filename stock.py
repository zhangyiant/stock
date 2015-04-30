import logging
from stock_gui.stock_app import StockApp

def main():
    logging.basicConfig(filename="stock.log", level=logging.DEBUG)
    logging.info("App started.")

    stock_app = StockApp()
    stock_app.mainloop()


if __name__ == "__main__":
    main()
