
insert into Customers values
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


insert into Products values
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


insert into Orders values
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




insert into OrderDetails values
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

insert into Inventory values
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

    
insert into Payments values(
500,1003,5000,'Processing ' ,'2024-03-02'),
(
501,1000,1000,'Completed ' ,'2024-02-02'),
(502,1001,53000,'Processing ' ,'2024-09-02'),
(503,1002,2500,'Completed ' ,'2024-05-12'),
(504,1004,20000,'Processing ' ,'2024-01-22')
