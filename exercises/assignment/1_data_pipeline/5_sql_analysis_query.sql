-- PostgreSQL analysis queries for your retail store chain dataset

-- Identifies which region generates the highest revenue
SELECT g.Region, SUM(rs.Sales) AS Total_Sales
FROM Retail_Sales rs
JOIN Geography g ON rs.PostalCode = g.PostalCode
GROUP BY g.Region
ORDER BY Total_Sales DESC;

-- determine the most popular products
SELECT rs.ProductName, SUM(rs.Sales) AS Total_Sales
FROM Retail_Sales rs
GROUP BY rs.ProductName
ORDER BY Total_Sales DESC
LIMIT 5;

-- Tracks seasonal sales trends.
SELECT OrderYear, OrderMonth, SUM(Sales) AS Monthly_Sales
FROM Retail_Sales
GROUP BY OrderYear, OrderMonth
ORDER BY OrderYear, OrderMonth;

-- Determines which customer segment is the most profitable
SELECT c.Segment, SUM(rs.Sales) AS Total_Sales, COUNT(DISTINCT rs.CustomerID) AS Total_Customers
FROM Retail_Sales rs
JOIN Customers c ON rs.CustomerID = c.CustomerID
GROUP BY c.Segment
ORDER BY Total_Sales DESC;

-- Identifies top revenue-generating cities
SELECT g.City, g.State, SUM(rs.Sales) AS Total_Sales
FROM Retail_Sales rs
JOIN Geography g ON rs.PostalCode = g.PostalCode
GROUP BY g.City, g.State
ORDER BY Total_Sales DESC
LIMIT 10;

-- measure the average revenue
SELECT AVG(Sales) AS Avg_Order_Value
FROM Retail_Sales;

-- Determines which product categories drive the most revenue
SELECT p.Category, SUM(rs.Sales) AS Total_Sales
FROM Retail_Sales rs
JOIN Products p ON rs.ProductID = p.ProductID
GROUP BY p.Category
ORDER BY Total_Sales DESC;

--Measures average delivery time 
SELECT EXTRACT(YEAR FROM OrderDate) AS Order_Year, 
       AVG(ShipDate - OrderDate) AS Avg_Delivery_Days
FROM Orders
GROUP BY Order_Year
ORDER BY Order_Year;


--Shows which shipping modes are most frequently used in high-value sales
SELECT o.ShipMode, SUM(rs.Sales) AS Total_Sales
FROM Retail_Sales rs
JOIN Orders o ON rs.OrderID = o.OrderID
GROUP BY o.ShipMode
ORDER BY Total_Sales DESC;



