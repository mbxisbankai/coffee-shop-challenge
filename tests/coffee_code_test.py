import pytest
from customer import Customer
from coffee import Coffee
from order import Order

# -------------------------------
# 1. Customer initializer & name
# -------------------------------
def test_customer_valid_name():
    c = Customer("Alice")
    assert c.name == "Alice"

def test_customer_invalid_name_type():
    with pytest.raises(ValueError):
        Customer(123)

def test_customer_invalid_name_length():
    with pytest.raises(ValueError):
        Customer("")

    with pytest.raises(ValueError):
        Customer("A" * 16)

def test_customer_name_setter_valid():
    c = Customer("Bob")
    c.name = "Billy"
    assert c.name == "Billy"

def test_customer_name_setter_invalid():
    c = Customer("Bob")
    with pytest.raises(ValueError):
        c.name = ""

# -------------------------------
# 2. Coffee initializer & name
# -------------------------------
def test_coffee_valid_name():
    cf = Coffee("Latte")
    assert cf.name == "Latte"

def test_coffee_invalid_name_type_or_length():
    with pytest.raises(ValueError):
        Coffee(123)
    with pytest.raises(ValueError):
        Coffee("Al")

def test_coffee_name_immutable():
    cf = Coffee("Mocha")
    with pytest.raises(AttributeError):
        cf.name = "Espresso"

# -------------------------------
# 3. Order initializer & price
# -------------------------------
def test_order_valid_init_and_price():
    c = Customer("Joe")
    cf = Coffee("Latte")
    o = Order(c, cf, 5.0)
    assert o.customer == c
    assert o.coffee == cf
    assert o.price == 5.0

def test_order_invalid_customer():
    cf = Coffee("Latte")
    with pytest.raises(TypeError):
        Order("NotCustomer", cf, 5.0)

def test_order_invalid_coffee():
    c = Customer("Joe")
    with pytest.raises(TypeError):
        Order(c, "NotCoffee", 5.0)

def test_order_invalid_price_type_or_range():
    c = Customer("Joe")
    cf = Coffee("Latte")
    with pytest.raises(ValueError):
        Order(c, cf, 0.5)
    with pytest.raises(ValueError):
        Order(c, cf, 11.0)
    with pytest.raises(ValueError):
        Order(c, cf, "Free")

def test_order_price_immutable():
    c = Customer("Joe")
    cf = Coffee("Latte")
    o = Order(c, cf, 5.0)
    with pytest.raises(AttributeError):
        o.price = 7.0

# -------------------------------
# 4. Relationship methods
# -------------------------------
def test_customer_orders_and_coffees():
    c = Customer("Ann")
    cf1 = Coffee("Latte")
    cf2 = Coffee("Espresso")
    c.create_order(cf1, 3.0)
    c.create_order(cf2, 4.0)
    c.create_order(cf1, 5.0)

    orders = c.orders()
    assert len(orders) == 3
    assert set(c.coffees()) == {cf1, cf2}

def test_coffee_orders_and_customers():
    c1 = Customer("John")
    c2 = Customer("Jane")
    cf = Coffee("Cappuccino")
    c1.create_order(cf, 4.5)
    c2.create_order(cf, 4.5)

    assert len(cf.orders()) == 2
    assert set(cf.customers()) == {c1, c2}

# -------------------------------
# 5. Aggregate/association methods
# -------------------------------
def test_customer_create_order():
    c = Customer("Testy")
    cf = Coffee("Flat White")
    o = c.create_order(cf, 6.0)
    assert isinstance(o, Order)
    assert o.customer == c
    assert o.coffee == cf

def test_coffee_num_orders_and_average_price():
    c = Customer("User")
    cf = Coffee("Latte")
    assert cf.num_orders() == 0
    assert cf.average_price() == 0.0

    c.create_order(cf, 3.0)
    c.create_order(cf, 5.0)
    assert cf.num_orders() == 2
    assert cf.average_price() == 4.0

# -------------------------------
# 6. Bonus: most_aficionado
# -------------------------------
def test_most_aficionado_returns_correct_customer():
    c1 = Customer("Ann")
    c2 = Customer("Ben")
    cf = Coffee("Macchiato")
    c1.create_order(cf, 3.0)
    c2.create_order(cf, 6.0)
    c2.create_order(cf, 2.0)

    assert Customer.most_aficionado(cf) == c2

def test_most_aficionado_none_if_no_orders():
    cf = Coffee("Ristretto")
    assert Customer.most_aficionado(cf) is None