

# TASK 1 DATABASE DESIGN
1. Create the database named "TechShop"
```
create database TechShop;
use TechShop;
```

![db](<Screenshot 2024-04-30 203600.png>)

2. Define the schema for the Customers, Products, Orders, OrderDetails and Inventory tables 
based on the provided schema.


>create table Customers(
     CustomerId int PRIMARY KEY,
	 FirstName text,
	 LastName text,
     Email varchar(50),
     Phone int,
     Address varchar(80)
);



>create table Products(
    ProductID int primary key,
    ProductName text,
    Description varchar(80),
    Price int
);


  
>create table Orders(
    OrderID int primary key,
    CustomerId int,
    OrderDate date,
    TotalAmount int,
    foreign key (CustomerId) references Customers(CustomerId)
);



>create table OrderDetails(
    OrderDetailID int primary key,
    OrderID int,
    ProductID int,
    Quantity int,
    foreign key (OrderID) references Orders(OrderID),
    foreign key (ProductID) references Products(ProductID)
);
   

>create table Inventory(
   InventoryId int primary key,
   ProductID int,
   QuantityInStock int,
   LastStockUpdate date,
   foreign key (ProductID) references products(ProductID)
);

>select* from Customers;
select * from Products;
select * from Orders;
select * from OrderDetails;
select* from Inventory;

3. Create an ERD (Entity Relationship Diagram) for the database.


![ERD](<Screenshot 2024-04-30 202950.png>)

4. Create appropriate Primary Key and Foreign Key constraints for referential integrity.
- foreign key (CustomerId) references Customers(CustomerId)
- foreign key (ProductID) references products(ProductID)
 - foreign key (OrderID) references Orders(OrderID),
 - foreign key (ProductID) references Products(ProductID)

5. Insert at least 10 sample records into each of the following tables.
- Customers

>insert into Customers values
    (10,'Abi' , 'Karthik' , 'abc@gmail.com', 98787887, 'XYZ street,chennai'),
    (11,'nadya' , 'khan' , 'fksejhf@gmail.com', 8762645, 'sdfs street,karnataka'),
    (12,'lolita' , 'nair' , 'ded@gmail.com', 7565568, 'fsd street,kanpur'),
    (13,'sharukh' , 'kapoor' , 'efg@gmail.com', 8476572, 'tfr street,ooty'),
    (14,'priya', 'dharshini' , 'aefa@gmail.com', 8765924, 'aaa street,madras'),
    (15,'nazeem' , 'tikar' , 'yuuu@gmail.com', 6533563, 'eee street,chennai'),
    (16,'narayan' , 'jahi' , 'fsfh@gmail.com', 689566, 'oooo street,karnataka'),
    (17,'lolita' , 'abishek' , 'lolo@gmail.com', 984586, 'lll street,kanpur'),
    (18,'sharukh' , 'saran' , 'abcaa@gmail.com', 9949994, 'awq street,ooty'),
    (19,'padma', 'shri' , 'jjj@gmail.com', 9327586, 'trrr street,madras'),
	(20,'kani' , 'ramya' , 'ahsj@gmail.com', 9494559, 'ijs street,kanpur'),
    (21,'kowshi', 'shri' , 'fdkj@gmail.com', 9489444, 'kkk street,madras'),
	(22,'kavya' , 'bala', 'kavya@gmail.com', 7675242, 'uuu street, nagpur');
;

- Products


>insert into Products values
    (100,' Monitor', 'displays output', 10000),
    (101,' keyboard', 'takes in input', 3000),
    (102,' Laptop', 'an electronic device', 100000),
    (103,' mouse', 'does click event', 1000),
    (104,' printer', 'prints ', 10430),
	(105,' cd', 'compact disk', 50),
    (106,' cpu', 'memory of pc', 1050),
    (107,' headphone', 'a device', 150),
    (108,' charger', 'portable one', 200),
    (109,' web cam', 'more clarity ', 5000);
    

- Orders


>insert into Orders values
    (1001, 10, '2012-01-12' , 24546),
    (1002, 11, '2020-12-10' , 27746),
    (1003, 12, '2020-03-16', 5452),
    (1004, 13, '2020-04-03', 45645),
    (1005, 14, '2021-06-20' , 233),
	(1006, 15, '2012-01-01' , 3434),
    (1007, 16, '2021-03-23' , 2334),
    (1008, 17, '2020-08-12', 567),
    (1009, 18, '2021-02-23', 123),
    (1010, 19, '2020-06-22' , 466),
    (1011, 20, '2020-06-02' , 4544),
	(1012, 21, '2020-06-09' , 567);


- OrderDetails

>insert into OrderDetails values
    (50, 1001, 100, 23),
    (51, 1002, 101, 12),
    (52, 1003, 102, 10),
    (53, 1004, 103, 24),
    (54, 1005, 104, 24),
	(60, 1006, 100, 23),
    (61, 1007, 105, 12),
    (62, 1008, 106, 10),
    (63, 1009, 107, 24),
    (64, 1010, 108, 24),
	(65, 1003, 102, 33),
	(66, 1010, 104, 25);

- Inventory

>insert into Inventory values
    (21,100,30,'2024-04-30'),
	(22,101,35,'2024-04-24'),
	(23,102,300,'2024-04-10'),
	(24,103,34,'2024-04-03'),
	(25,104,73,'2024-04-04'),
	(26,105,563,'2024-04-17'),
	(27,106,453,'2024-04-23'),
	(28,107,346,'2024-04-27'),
	(29,108,256,'2024-04-02'),
	(30,109,89,'2024-04-06');


# Tasks 2: Select, Where, Between, AND, LIKE

1. Write an SQL query to retrieve the names and emails of all customers. 

>select FirstName, LastName, email from Customers;

2. Write an SQL query to list all orders with their order dates and corresponding customer 
names.

>select OrderId, OrderDate, FirstName,LastName from orders
right join customers on
orders.CustomerId = Customers.CustomerId
;

3. Write an SQL query to insert a new customer record into the "Customers" table. Include customer information such as name, email, and address.

>insert into Customers values(23, 'nadya' , 'ram' , 'nadra@gmail.com', 4647646, 'ise street,haryana');

4. Write an SQL query to update the prices of all electronic gadgets in the "Products" table by 
increasing them by 10%.

>update Products
set price *=  0.1;

5. Write an SQL query to delete a specific order and its associated order details from the 
"Orders" and "OrderDetails" tables. Allow users to input the order ID as a parameter.

>declare @oh int = 1008;
delete from orderdetails
where orderid = @oh;
delete from orders
where orderid = @oh;


6. Write an SQL query to insert a new order into the "Orders" table. Include the customer ID, 
order date, and any other necessary information.

>insert into orders values( 1013 , 23, '2020-03-06',443);

7. Write an SQL query to update the contact information (e.g., email and address) of a specific 
customer in the "Customers" table. Allow users to input the customer ID and new contact 
information.
```
declare @up int = 17;
update customers
set email = 'lolii@gmail.com',
address = 'nami street,canada'
where customerid = @up;

```

8. Write an SQL query to recalculate and update the total cost of each order in the "Orders" 
table based on the prices and quantities in the "OrderDetails" table.
```

--step 1
select price * quantity
from products
right join OrderDetails on
Products.ProductID = OrderDetails.ProductID;

--final ans
update orders
set totalamount = (select sum(price * quantity)  from products
right join OrderDetails on
Products.ProductID = OrderDetails.ProductID
where orders.orderid = orderdetails.orderid);
```
9. Write an SQL query to delete all orders and their associated order details for a specific 
customer from the "Orders" and "OrderDetails" tables. Allow users to input the customer ID 
as a parameter.
```
declare @de int = 16;
delete from orderdetails 
where orderid = (select orderid from orders
where customerid = @de);
delete from orders
where customerid = @de;
```
10. Write an SQL query to insert a new electronic gadget product into the "Products" table, 
including product name, category, price, and any other relevant details.
```

alter table products
add category text;


UPDATE Products
SET Category = 'Electronic Gadgets'
WHERE ProductID IN (102, 103, 104, 106, 109);
update products
set category = 'not an electronic gadget '
where ProductID in ( 100,101,105,107,108);

insert into products values(110,'keys','for typing',234,'not an electronic gadget');

```

11. Write an SQL query to update the status of a specific order in the "Orders" table (e.g., from 
"Pending" to "Shipped"). Allow users to input the order ID and the new status.
```
alter table orders
add status text;

update orders
set status = 'Pending'
declare @ohs int = 1005;
update orders
set status = 'Shipped'
where orderid = @ohs;
select* from orders;
```
12. Write an SQL query to calculate and update the number of orders placed by each customer 
in the "Customers" table based on the data in the "Orders" table.

```

select customers.customerid,count(orderid) from orders
right join customers on
orders.customerid = Customers.CustomerId
group by customers.CustomerId
;

```

# Task 3. Aggregate functions, Having, Order By, GroupBy and Joins:
1. Write an SQL query to retrieve a list of all orders along with customer information (e.g., 
customer name) for each order.
```
select*  from orders
inner join Customers on
orders.CustomerId = Customers.CustomerId;
```
2. Write an SQL query to find the total revenue generated by each electronic gadget product. 
Include the product name and the total revenue.
```
select products.productname, orders.totalamount from orders
inner join orderdetails on
orders.orderID = orderdetails.orderid

right join products on
orderdetails.productID = products.productID
;
```
3.  Write an SQL query to list all customers who have made at least one purchase. Include their 
names and contact information.
```
select * from Customers
left join orders on 
customers.CustomerId = orders.CustomerId
where TotalAmount>1;
```
4. Write an SQL query to find the most popular electronic gadget, which is the one with the highest 
total quantity ordered. Include the product name and the total quantity ordered.
```
select productname , (select max(quantity)from OrderDetails) as maxi from Products
where productid = (select productid from orderdetails
order by Quantity desc
offset 0 rows
fetch next 1 rows only);
```

5. Write an SQL query to retrieve a list of electronic gadgets along with their corresponding 
categories.
```
select productname,category from products;
```
6. Write an SQL query to calculate the average order value for each customer. Include the 
customer's name and their average order value.
```
select firstname ,totalamount from customers
right join orders on
customers.CustomerId= orders.customerid
where totalamount in(
select avg((totalamount)/count(orderdetails.orderid)) as av from orders
right join OrderDetails on orders.OrderId=OrderDetails.OrderID
group by orders.OrderID);
```
7. Write an SQL query to find the order with the highest total revenue. Include the order ID, 
customer information, and the total revenue.
```
select *  from orders
right join customers on
orders.CustomerId = customers.customerID
order by TotalAmount desc
offset 0 rows
fetch next 1 rows only;
```
8. Write an SQL query to list electronic gadgets and the number of times each product has been 
ordered.
```
select productname , (
select count(productid) from OrderDetails i
where i.ProductID= o.productid
group by ProductID) from products o
where category like 'Electronic Gadgets'
;
```
9. Write an SQL query to find customers who have purchased a specific electronic gadget product. 
Allow users to input the product name as a parameter.
```
declare @yee text = 'mouse';
select firstname from customers
where customerid in (select customerid from orders
where orderid in (select orderid from OrderDetails
where productid in ( select productid from products
where ProductName = @yee)));
```
10. Write an SQL query to calculate the total revenue generated by all orders placed within a 
specific time period. Allow users to input the start and end dates as parameters.
```

declare @st date = '2012-01-01';
declare @en date =  '2020-02-23';
select sum(totalamount) from orders
where orderdate between @st and @en;
```
# Task 4. Subquery and its type:
1. Write an SQL query to find out which customers have not placed any orders.
```
select firstname , customerid from customers
where customerid not in ( select customerid from orders);
```

2. Write an SQL query to find the total number of products available for sale. 
```
select sum(quantityinstock) from inventory;
```
3. Write an SQL query to calculate the total revenue generated by TechShop. 
```
select sum(totalamount) from orders;
```
4. Write an SQL query to calculate the average quantity ordered for products in a specific category. 
Allow users to input the category name as a parameter.
```
declare @ush varchar(max) = 'Electronic Gadgets';
select avg(quantity) as av from orderdetails
right join products on
OrderDetails.ProductID = Products.ProductID
where category like @ush
;
```
5. Write an SQL query to calculate the total revenue generated by a specific customer. Allow users 
to input the customer ID as a parameter.
```
declare @rev int = 12
select totalamount from orders
where customerid = @rev;
```
6. Write an SQL query to find the customers who have placed the most orders. List their names 
and the number of orders they've placed.
```
select firstname , (select (count(*)) from orders 
where orders.CustomerId= customers.CustomerId) as coun from customers
order by coun desc
offset 0 rows
fetch next 1 rows only;
```
7. Write an SQL query to find the most popular product category, which is the one with the highest 
total quantity ordered across all orders.
```
select category from products
right join OrderDetails on
Products.ProductID= OrderDetails.ProductID
where Quantity in(
select max(quantity) from OrderDetails);
```
8. Write an SQL query to find the customer who has spent the most money (highest total revenue) 
on electronic gadgets. List their name and total spending.
```
select customers.firstname, orders.totalamount from customers
right join orders on
customers.CustomerId= orders.CustomerId
where totalamount in
(select
max(totalamount) from orders) ;
```
9. Write an SQL query to calculate the average order value (total revenue divided by the number of 
orders) for all customers.
```
  everyone has only 1 orders so:::
select avg(totalamount) from orders
group by orderid;
```
10. Write an SQL query to find the total number of orders placed by each customer and list their 
names along with the order count
```
select customers.CustomerId,count(orders.OrderID) as coo from customers 
inner join orders on
Customers.CustomerId=orders.CustomerId
group by Customers.CustomerId
order by Customers.CustomerId;
```