class Coffee:

    def __init__(self, name):

        if isinstance(name, str) and 3 <= len(name):
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")
        self.orders = []
        self.customers = []

    @property
    def name(self):
        return self._name
    
    def average_price(self):
        if not self.orders:
            return 0
        total_price = sum(order.price for order in self.orders)
        return total_price / len(self.orders)

    def num_orders(self):
        return len(self.orders)
    

    
