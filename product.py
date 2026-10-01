class product:
    def __init__(self,code, name, price):
        self.code = code
        self.name = name
        self.price = price
    def get_price_it():
        tax = 0.2
        return self.price + (self.price * tax)
product = product()
print(f"{product.code} - {product.name} - {product.price}")

