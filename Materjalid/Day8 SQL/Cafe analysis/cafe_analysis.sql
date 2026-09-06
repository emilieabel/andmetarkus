-- Analyze cafe sales and compare them to budget 

-- 1.1. Cafe sales by Year-Month 
SELECT TO_CHAR(transaction_date, 'YYYY-MM') sale_month, 
SUM(total_spent_calc) AS sale_sum
FROM cafe_sales_cleaned
GROUP BY sale_month
ORDER BY sale_month;

-- 1.2. Monthly sales vs monthly budget 
WITH monthly_sales AS (SELECT TO_CHAR(transaction_date, 'YYYY-MM') sale_month, 
SUM(total_spent_calc) AS sale_sum
FROM cafe_sales_cleaned
GROUP BY sale_month
ORDER BY sale_month)
SELECT m.sale_month, m.sale_sum, budget_sum
FROM cafe_budget AS b
LEFT JOIN monthly_sales AS m
ON b.year_month = m.sale_month;

-- 1.3. Cafe sales by item 
SELECT item_cleaned, SUM(total_spent_calc) AS sale_sum
FROM cafe_sales_cleaned
GROUP BY item_cleaned
ORDER BY item_cleaned;

-- 1.4. Compare average sale sum per item to average sale sum for all items 
SELECT item_cleaned, ROUND(AVG(total_spent_calc),2) AS avg_sale_sum_per_item, 
(SELECT ROUND(AVG(total_spent_calc), 2) as total_average FROM cafe_sales_cleaned), 
ROUND(AVG(total_spent_calc) - (SELECT AVG(total_spent_calc) as total_average FROM cafe_sales_cleaned), 2) AS diff_from_avg_sale
FROM cafe_sales_cleaned 
GROUP BY item_cleaned
ORDER BY diff_from_avg_sale DESC;

-- 1.5. Filter out only items where  sales were more than 10 000
SELECT item_cleaned, SUM(total_spent_calc) AS sale_sum
FROM cafe_sales_cleaned
GROUP BY item_cleaned
HAVING SUM(total_spent_calc) > 10000
ORDER BY item_cleaned;

-- 1.6. What were sales by payment method?
SELECT payment_method_cleaned , SUM(total_spent_calc) AS sale_sum
FROM cafe_sales_cleaned
GROUP BY payment_method_cleaned
ORDER BY payment_method_cleaned;

-- 1.7. Compare average sale sum by location to average sale sum
SELECT location_cleaned, ROUND(AVG(total_spent_calc),2) AS avg_sale_sum_per_location, 
(SELECT ROUND(AVG(total_spent_calc), 2) as total_average FROM cafe_sales_cleaned), 
ROUND(AVG(total_spent_calc) - (SELECT AVG(total_spent_calc) AS total_average FROM cafe_sales_cleaned), 2) AS diff_from_avg_sale
FROM cafe_sales_cleaned 
GROUP BY location_cleaned
ORDER BY diff_from_avg_sale DESC;

-- 1.8. What were sales by location?
SELECT location_cleaned , SUM(total_spent_calc) AS sale_sum
FROM cafe_sales_cleaned
GROUP BY location_cleaned
ORDER BY location_cleaned;

-- 1.9. How many units per item were sold?
SELECT item_cleaned , SUM(quantity) AS quantity
FROM cafe_sales_cleaned
GROUP BY item_cleaned
ORDER BY item_cleaned;

-- 1.10. Filter out only items where more than 3000 units were sold
SELECT item_cleaned , SUM(quantity) AS quantity
FROM cafe_sales_cleaned
GROUP BY item_cleaned
HAVING SUM(quantity) > 3000
ORDER BY item_cleaned;