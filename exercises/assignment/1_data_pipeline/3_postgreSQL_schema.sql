-- PostgreSQL schema for retail analytics, defining dimension tables for customers, geography, products, 
-- and orders, along with a fact table for sales data. 

ALTER DEFAULT PRIVILEGES IN SCHEMA public 
GRANT INSERT, UPDATE, DELETE ON  TABLES TO retail_db_user;

-- PostgreSQL Schema for Retail Analytics

-- Customer Table
CREATE TABLE Customers (
    CustomerID VARCHAR PRIMARY KEY,
    CustomerName VARCHAR NOT NULL,
    Segment VARCHAR CHECK (Segment IN ('Consumer', 'Corporate', 'Home Office'))
);

-- Geography Table
CREATE TABLE Geography (
    PostalCode VARCHAR PRIMARY KEY,
    City VARCHAR NOT NULL,
    State VARCHAR NOT NULL,
    Region VARCHAR CHECK (Region IN ('West', 'East', 'Central', 'South'))
);

-- Product Table
CREATE TABLE Products (
    ProductID VARCHAR NOT NULL,
    ProductName VARCHAR NOT NULL,
    SubCategory VARCHAR NOT NULL,
    Category VARCHAR CHECK (Category IN ('Furniture', 'Office Supplies', 'Technology')),
    PRIMARY KEY (ProductID,ProductName)
);

-- Order Table
CREATE TABLE Orders (
    OrderID VARCHAR PRIMARY KEY,
    OrderDate DATE NOT NULL,
    ShipDate DATE NOT NULL,
    ShipMode VARCHAR CHECK (ShipMode IN ('First Class', 'Second Class', 'Standard Class', 'Same Day'))
);



-- Fact Table: Sales

CREATE TABLE Retail_Sales (
    RowID SERIAL PRIMARY KEY,
    OrderID VARCHAR NOT NULL,
    CustomerID VARCHAR NOT NULL,
    PostalCode VARCHAR NOT NULL,
    ProductID VARCHAR NOT NULL,
    ProductName VARCHAR NOT NULL,
    Sales DECIMAL(10,2) NOT NULL CHECK (Sales >= 0), 
    OrderYear INT CHECK (OrderYear BETWEEN 2000 AND 2100),
    OrderMonth INT CHECK (OrderMonth BETWEEN 1 AND 12),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE,
    FOREIGN KEY (PostalCode) REFERENCES Geography(PostalCode) ON DELETE CASCADE,
    FOREIGN KEY (ProductID, ProductName) REFERENCES Products(ProductID, ProductName) ON DELETE CASCADE
);


select*from retail_sales;


