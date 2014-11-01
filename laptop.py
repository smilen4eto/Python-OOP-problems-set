class Product:

    def __init__(self, name, stock_price, final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        return self.final_price - self.stock_price


class Laptop(Product):
    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price, display_size, mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    def __init__(self, name):
        self.name = name
        self.items = {}
        self.income = 0

    def load_new_products(self, item, count):
            if item in self.items:
                self.items[item] += count
            else:
                self.items[item] = count

    def list_products(self, item_class):
        for item in self.items:
            if isinstance(item, item_class):
                print(item.name)

    def sell_products(self, product):
        if product in self.items and self.items[product] > 0:
            self.items[product] -= 1
            self.income += product.profit()
            return True
        else:
            return False

    def total_income(self):
        return self.income

store = Store('Laptop.bg')
smartphone = Smartphone('Hack Phone', 500, 820, 7, 10)
laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)
store.load_new_products(smartphone, 2)
print(store.sell_products(smartphone))
print(store.sell_products(smartphone))
print(store.total_income())
