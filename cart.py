class Cart:
    def __init__(self):
        self.cart_items = []

    def add_product(self, product):
        self.cart_items.append(product)

    def total_price(self):
        return sum(p.price for p in self.cart_items)

    def show_cart(self):
        for product in self.cart_items:
            print(product.display_info())
