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

    def update_product(self, product_name, new_quantity):
        for product in self.products:
            if product.name == product_name:
                product.quantity = new_quantity

class Supplier:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

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

    def add_product_to_stock(self, product):
        self.stock.add_product(product)

    def remove_product_from_stock(self, product_name):
        self.stock.remove_product(product_name)

    def update_product_quantity(self, product_name, new_quantity):
        self.stock.update_product(product_name, new_quantity)

    def display_stock(self):
        for product in self.stock.products:
            print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

    def display_suppliers(self):
        for supplier in self.suppliers:
            print(f"Supplier: {supplier.name}, Phone Number: {supplier.phone_number}")

system = InventoryManagementSystem()
product1 = Product("Product1", 100, 10)
product2 = Product("Product2", 200, 20)
supplier1 = Supplier("Supplier1", "1234567890")
supplier2 = Supplier("Supplier2", "9876543210")

system.add_product_to_stock(product1)
system.add_product_to_stock(product2)
system.add_supplier(supplier1)
system.add_supplier(supplier2)

system.display_stock()
system.display_suppliers()

system.update_product_quantity("Product1", 15)
system.remove_product_from_stock("Product2")
system.remove_supplier("Supplier1")

system.display_stock()
system.display_suppliers()