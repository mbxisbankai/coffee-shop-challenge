from customer import Customer
from coffee import Coffee

class Order:
    num_of_orders = 0

    def __init__(self, customer, coffee, price):
        if isinstance(customer, Customer):
            self._customer = customer
            customer.orders.append(self)
        else:
            raise TypeError('Customer must be an instance of the Customer Class.')
        if isinstance(coffee, Coffee):
            self._coffee = coffee
            coffee.orders.append(self)
        else:
            raise TypeError('Coffee must be an instance of the Coffee Class.')
        if isinstance(price, (int, float)) and 10 <= price <= 100:
            self.price = price
        else:
            raise ValueError('Please enter a valid price.')
        
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
    
