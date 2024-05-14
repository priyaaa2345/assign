class Inventory:
    def __init__(self, InventoryID, ProductID, QuantityInStock, LastStockUpdate):
        self.__InventoryID = InventoryID
        self.__ProductID = ProductID
        self.QuantityInStock = QuantityInStock
        self.LastStockUpdate = LastStockUpdate

    def get_inventoryid(self):
        return self.__InventoryID

    def set_inventoryid(self, InventoryID):
        self.__InventoryID = InventoryID

    def get_ProductID(self):
        return self.__ProductID

    def set_ProductID(self, ProductID):
        self.__ProductID = ProductID
