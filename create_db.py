import sqlite3

# Create database
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create sales table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sample_data = [
    ('Apple', 10, 15.0),
    ('Banana', 20, 5.0),
    ('Orange', 15, 8.0),
    ('Apple', 5, 15.0),
    ('Banana', 10, 5.0),
    ('Orange', 5, 8.0),
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sample_data)
conn.commit()
conn.close()
print("Database created with sample data.")
