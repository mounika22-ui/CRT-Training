class InvalidProductIndexError(Exception):
    pass
class OutOfStockError(Exception):
    pass
class InvalidQuantityError(Exception):
    pass
class EmptyInventoryError(Exception):
    pass
class Inventory:
    def __init__(self, products):
        self.products = products
    def purchase(self, index, quantity):
        if len(self.products) == 0:
            raise EmptyInventoryError("Inventory is empty.")
        if index < 0 or index >= len(self.products):
            raise InvalidProductIndexError("Invalid product index.")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0.")
        if quantity > self.products[index]:
            raise OutOfStockError("Requested quantity exceeds available stock.")
        self.products[index] -= quantity
        print(self.products)
n = int(input())
products = list(map(int, input().split()))
index = int(input())
quantity = int(input())
obj = Inventory(products)
try:
    obj.purchase(index, quantity)
except InvalidProductIndexError as e:
    print("InvalidProductIndexError:", e)
except OutOfStockError as e:
    print("OutOfStockError:", e)
except InvalidQuantityError as e:
    print("InvalidQuantityError:", e)
except EmptyInventoryError as e:
    print("EmptyInventoryError:", e)