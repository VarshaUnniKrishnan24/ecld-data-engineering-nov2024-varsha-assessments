CREATE TABLE customers (
customer_id SERIAL PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
signup_date DATE,
total_purchases INTEGER,
last_purchase_date DATE
);

INSERT INTO customers (first_name, last_name, signup_date, total_purchases,
last_purchase_date) VALUES
('John', 'Doe', '2023-01-15', 25, '2024-03-15'),
('Jane', 'Smith', '2023-02-01', 15, '2023-12-20'),
('Bob', 'Johnson', '2023-03-10', 8, '2024-02-28'),
('Alice', 'Brown', '2023-04-05', 30, '2024-03-10'),
('Charlie', 'Wilson', '2023-05-20', 12, '2023-11-15');

	
	WITH customer_segments AS (
    SELECT 
        customer_id,
        first_name,
        last_name,
        signup_date,
        total_purchases,
        last_purchase_date,
        CASE
            WHEN last_purchase_date >= CURRENT_DATE - INTERVAL '90 days' THEN 'Active'
            ELSE 'Churned'
        END AS status,
        DATE_PART('month', AGE(CURRENT_DATE, signup_date)) AS months_since_signup
    FROM 
        customers
),
aggregated_segments AS (
    SELECT
        status,
        COUNT(customer_id) AS customer_count,
        AVG(total_purchases) AS avg_purchases,
        AVG(total_purchases::float / NULLIF(months_since_signup, 0)) AS avg_monthly_purchase_freq
    FROM
        customer_segments
    GROUP BY
        status
)
SELECT
    status,
    customer_count,
    avg_purchases,
    avg_monthly_purchase_freq
FROM
    aggregated_segments
ORDER BY
    status;
