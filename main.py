class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Stock:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product_name):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                break

    def update_product_quantity(self, product_name, quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity = quantity
                break

class Supplier:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class InventoryManagementSystem:
    def __init__(self):
        self.stock = Stock()
        self.suppliers = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def remove_supplier(self, supplier_name):
        for supplier in self.suppliers:
            if supplier.name == supplier_name:
                self.suppliers.remove(supplier)
                break

    def display_stock(self):
        for product in self.stock.products:
            print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def display_suppliers(self):
        for supplier in self.suppliers:
            print(f"Supplier: {supplier.name}, Address: {supplier.address}")

ims = InventoryManagementSystem()
product1 = Product("Laptop", 1000, 10)
product2 = Product("Phone", 500, 20)
supplier1 = Supplier("Apple", "New York")
supplier2 = Supplier("Samsung", "Seoul")

ims.stock.add_product(product1)
ims.stock.add_product(product2)
ims.add_supplier(supplier1)
ims.add_supplier(supplier2)

ims.display_stock()
ims.display_suppliers()

ims.stock.update_product_quantity("Laptop", 5)
ims.remove_supplier("Samsung")

ims.display_stock()
ims.display_suppliers()