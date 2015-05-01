import logging
from stock_gui.stock_app import StockApp

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
    fh = logging.FileHandler('stock.log', encoding="utf-8")
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logging.info("App started.")
    stock_app = StockApp()
    stock_app.mainloop()


if __name__ == "__main__":
    main()
