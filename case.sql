create table Customer(
CustomerID int primary key,
FirstName varchar(80),
LastName varchar(80),
Email varchar(100),
PhoneNumber bigint,
Address varchar(100),
Username varchar(100),
Password varchar(255),
RegistrationDate date
);

create table Vehicle(
VehicleID varchar(100) primary key,
Model varchar(100),
Make text,
Year int,
Color text,
RegistrationNumber int unique,
Availability BIT,
DailyRate int
);

create table Reservation(
ReservationID varchar(100) primary key,
CustomerID int,
VehicleID varchar(100),
StartDate datetime,
EndDate datetime,
TotalCost int,
Status text,
foreign key (CustomerID) references Customer(CustomerID),
foreign key (VehicleID) references Vehicle(VehicleID)

);

create table Admin(
AdminID varchar(50) primary key,
FirstName varchar(100),
LastName varchar(100),
Email varchar(255),
PhoneNumber bigint,
Username varchar(100),
Password varchar(255),
Role text,
JoinDate date
);

select * from customer;
select * from Vehicle;
select * from Reservation;
select * from Admin;