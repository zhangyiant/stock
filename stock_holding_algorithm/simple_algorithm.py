class simple_algorithm:
    def __init__(self, start_price, stop_price):
        self.start_price = start_price
        self.stop_price = stop_price

    def get_percentage(self, current_price):
        if current_price < self.start_price:
            return 0
        if current_price > self.start_price:
            return 100
        
    def print(self):
        print(self.start_price, self.stop_price)

