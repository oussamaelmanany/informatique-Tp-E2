class product:
    tax = 0.2
    def __init__(self,code, name, price):
        self.code = code
        self.name = name
        self.price = price
    def get_price_it(self):
        return self.price + (self.price * tax)
product = product()
print(f"{product.code} - {product.name} - {product.price}")

