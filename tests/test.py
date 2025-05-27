from customer import Customer
from coffee import Coffee
from order import Order

# Create customers
alice = Customer("Alice")
bob = Customer("Bob")

# Create coffee types
espresso = Coffee("Espresso")
latte = Coffee("Latte")

# Create orders
order1 = alice.create_order(espresso, 25)
order2 = alice.create_order(latte, 30)
order3 = bob.create_order(espresso, 45)

# Check orders
print(f"Alice's orders: {[o.coffee.name for o in alice.orders]}")
print(f"Bob's orders: {[o.coffee.name for o in bob.orders]}")

# Check most aficionado
aficionado = Customer.most_aficionado(espresso)
print(f"Most aficionado for Espresso: {aficionado.name if aficionado else 'None'}")

# Check relationships
print(f"Espresso customers: {[c.name for c in espresso.customers]}")
print(f"Latte customers: {[c.name for c in latte.customers]}")
