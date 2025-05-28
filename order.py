from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from customer import Customer
    from coffee import Coffee

class Order:
    num_of_orders = 0

    def __init__(self, customer, coffee, price):
    
        from customer import Customer
        from coffee import Coffee


        if not isinstance(customer, Customer):
            raise TypeError('Customer must be an instance of the Customer Class.')

        if not isinstance(coffee, Coffee):
            raise TypeError('Coffee must be an instance of the Coffee Class.')

        if not isinstance(price, (int, float)) and 10 <= price <= 100:
            raise ValueError('Please enter a valid price.')
            
        self._coffee = coffee
        self._customer = customer
        self.price = price

        if coffee not in customer.coffees:
            customer.coffees.append(coffee)
        if customer not in coffee.customers:
            coffee.customers.append(customer)

        Order.num_of_orders += 1

    @property
    def coffee(self):
        return self._coffee

    @property
    def customer(self):
        return self._customer

