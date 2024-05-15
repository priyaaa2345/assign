create table Customers(
     CustomerId int PRIMARY KEY,
	 FirstName text,
	 LastName text,
     Email varchar(50),
     Phone int,
     Address varchar(80)
);


create table Products(
    ProductID int primary key,
    ProductName text,
    Description varchar(80),
    Price int
);


create table Orders(
    OrderID int primary key,
    CustomerId int,
    OrderDate date,
    TotalAmount int,
    foreign key (CustomerId) references Customers(CustomerId)
);



create table OrderDetails(
    OrderDetailID int primary key,
    OrderID int,
    ProductID int,
    Quantity int,
    foreign key (OrderID) references Orders(OrderID),
    foreign key (ProductID) references Products(ProductID)
);


create table Inventory(
   InventoryId int primary key,
   ProductID int,
   QuantityInStock int,
   LastStockUpdate date,
   foreign key (ProductID) references products(ProductID)
);