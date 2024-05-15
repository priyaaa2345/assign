class Inventory:
    def __init__(
        self, InventoryID, ProductID, QuantityInStock, LastStockUpdate, product
    ):
        self.__InventoryID = InventoryID
        self.__ProductID = ProductID
        self.QuantityInStock = QuantityInStock
        self.LastStockUpdate = LastStockUpdate
        self.product = product

    def get_inventoryid(self):
        return self.__InventoryID

    def set_inventoryid(self, InventoryID):
        self.__InventoryID = InventoryID

    def get_ProductID(self):
        return self.__ProductID

    # for task collections
    def set_ProductID(self, ProductID):
        self.__ProductID = ProductID

    def set_sort_inventory(self, InventoryID):
        self.__InventoryID = InventoryID

    # task 4 composition
    def get_product(self, product):
        self.product = product
