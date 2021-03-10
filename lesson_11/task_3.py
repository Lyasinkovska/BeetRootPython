"""
Product Store

Write a class Product that has three attributes:

type name price Then create a class ProductStore, which will have some Products and will operate with all products in
the store. All methods, in case they can’t perform its action, should raise ValueError with appropriate error
information.

Tips: Use aggregation/composition concepts while implementing the ProductStore class. You can also implement
additional classes to operate on a certain type of product, etc.

Also, the ProductStore class must have the following methods:

add(product, amount) - adds a specified quantity of a single product with a predefined price premium for your store(
        30 percent)
set_discount(identifier, percent, identifier_type=’name’) - adds a discount for all products specified by
        input identifiers (type or name). The discount must be specified in percentage
sell_product(product_name,amount) - removes a particular amount of products from the store if available, in other case
        raises an error. It also increments income if the sell_product method succeeds.
get_income() - returns amount of many earned by ProductStore instance.
get_all_products() - returns information about all available products in the store.
get_product_info(product_name) - returns a tuple with product name and amount of items in the store. ```

"""


class Product:
    def __init__(self, product_type='', name='', price=0):
        self.product_type = product_type
        self.name = name
        self.price = price


class StoreProduct:

    def __init__(self, prod: Product):
        self.prod = prod
        self.price = prod.price
        self.name = self.prod.name
        self.premium = 30
        self.amount = 0

    @property
    def hash(self):
        return self.name, self.prod.product_type

    def set_shop_price(self, premium: int or float):
        return round(self.price * (1 + premium / 100), 2)

    def current_shop_price(self, old_price, premium=30):
        return max(old_price, self.set_shop_price(premium))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.prod.product_type}, {self.prod.name}, {self.price}, {self.amount}"


class ProductStore:

    def __init__(self):
        self.products = {}
        self.income = 0
        self.premium = 30

    def add(self, product: Product, amount: int):
        shop_product = StoreProduct(product)
        shop_key = shop_product.hash
        if shop_product.hash not in self.products.keys():
            self.products.update({shop_key: shop_product})
            shop_product.amount = amount
            shop_product.price = shop_product.set_shop_price(self.premium)
        else:
            self.products[shop_key].amount += amount
            self.products[shop_key].price = shop_product.current_shop_price(self.products[shop_key].price)

    def set_discount(self, identifier, percent, identifier_type='name'):
        for key, product in self.products.items():
            if identifier in key:
                product.price = product.set_shop_price(-percent)

    def sell_product(self, product_name, amount):
        for key, product in self.products.items():
            if product_name in key[0] and amount <= product.amount:
                product.amount -= amount
                self.income += product.price * amount
                break
            else:
                raise ValueError('No such product found.')

    def get_income(self):
        return self.income

    def get_all_products(self):
        return self.products

    def get_product_info(self, product_name):
        try:
            for key, product in self.products.items():
                if product_name in key[0]:
                    return product.name, product.amount
        except Exception:
            raise ValueError("There is no such product in a store.")


if __name__ == '__main__':
    store = ProductStore()
    p = Product('Food', 'Ramen', 2)
    p3 = Product('Food', 'Ramen', 10)
    p2 = Product('Food', 'Pasta', 5)
    p4 = Product('Sport', 'Jeans', 150)
    store.add(p, 100)
    store.add(p, 20)
    store.add(p3, 20)
    store.add(p2, 50)
    store.add(p4, 10)
    print(store.products)
    store.set_discount('Food', 10)
    store.sell_product('Ramen', 50)
    print(store.income)
    print(store.products)
    print(store.get_product_info('Ramen'))


