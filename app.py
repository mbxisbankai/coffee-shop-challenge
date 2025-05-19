from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffee types
latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
alice.create_order(latte, 15.0)
alice.create_order(latte, 12.5)
bob.create_order(latte, 20.0)
bob.create_order(espresso, 18.0)

# Test most_aficionado method
top_customer = Customer.most_aficionado(latte)
print(f"The most aficionado for Latte is: {top_customer.name}")
