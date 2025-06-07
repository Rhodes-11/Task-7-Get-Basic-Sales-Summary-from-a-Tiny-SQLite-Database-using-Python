import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create table and insert sample data
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

sample_data = [
    ('Pen', 10, 5.0),
    ('Pencil', 20, 2.5),
    ('Notebook', 5, 20.0),
    ('Pen', 15, 5.0),
    ('Pencil', 10, 2.5),
    ('Notebook', 7, 20.0)
]
cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()

# SQL query
query = (
    "SELECT product, "
    "SUM(quantity) AS total_qty, "
    "SUM(quantity * price) AS revenue "
    "FROM sales GROUP BY product"
)

# Load into pandas and close connection
df = pd.read_sql_query(query, conn)
conn.close()

# Print the summary
print(df)

# Plot the revenue
df.plot(kind='bar', x='product', y='revenue', legend=False)
plt.title("Revenue per Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()
