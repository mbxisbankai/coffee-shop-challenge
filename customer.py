class Customer:
    all = []

    def __init__(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError('Enter a valid name.')
        self.orders = []
        self.coffees = []
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:
            raise ValueError('Name must be a string between 1 and 15 characters.')

    def create_order(self, coffee, price):
        from order import Order  # kept as local import
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        max_spender = None
        max_spent = 0

        for customer in cls.all:
            total_spent = sum(
                order.price for order in customer.orders if order.coffee == coffee
            )
            if total_spent > max_spent:
                max_spent = total_spent
                max_spender = customer

        return max_spender



