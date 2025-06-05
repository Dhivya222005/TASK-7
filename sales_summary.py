
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("sales_data.db")

# SQL query to get total quantity and revenue per product
query = """
SELECT product, 
       SUM(quantity) AS total_qty, 
       SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Run query and load into pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print DataFrame
print("Sales Summary:")
print(df)

# Plot bar chart
df.plot(kind='bar', x='product', y='revenue', title='Revenue by Product', color='skyblue')
plt.ylabel("Revenue")
plt.tight_layout()

# Save chart as image
plt.savefig("sales_chart.png")
plt.show()

# Close connection
conn.close()
