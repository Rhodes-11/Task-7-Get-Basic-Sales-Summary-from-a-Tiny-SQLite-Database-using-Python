# Task 7 - Basic Sales Summary using Python and SQLite

## Objective
To analyze a small sales dataset stored in SQLite, compute total quantities and revenue per product, and visualize the results using a bar chart.

## Tools Used
- Python
- SQLite (via `sqlite3`)
- Pandas
- Matplotlib

## Steps
1. Created a database `sales_data.db` with a `sales` table.
2. Inserted sample product data.
3. Queried the data using SQL to calculate:
   - Total quantity sold per product
   - Total revenue per product
4. Loaded the result into a pandas DataFrame.
5. Displayed the result and plotted a bar chart showing revenue.

## SQL Query Used
```sql
SELECT product, SUM(quantity) AS total_qty, SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product;
