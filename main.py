from product import Product
from product_manager import ProductManager
from cart import Cart


manager = ProductManager()

p1 = Product("Laptop", 1000, 5)
p2 = Product("Telefon", 500, 10)
p3 = Product("Mis", 20, 50)

manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

manager.show_products()
print("Ukupna vrednost inventara:", manager.total_inventory_value())

cart = Cart()
cart.add_product(p1)
cart.add_product(p2)
cart.add_product(p3)

cart.show_cart()
print("Ukupno za naplatu:", cart.total_price())
