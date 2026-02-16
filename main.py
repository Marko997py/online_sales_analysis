from product import Product
from product_manager import ProductManager

manager = ProductManager()

p1 = Product("Laptop Pro", 1200, 3)
p2 = Product("Telefon X", 700, 5)
p3 = Product("Mis", 20, 50)


manager.add_product(p1)
manager.add_product(p2)
manager.add_product(p3)

