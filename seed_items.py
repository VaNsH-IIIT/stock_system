import sqlite3

# Item data: (barcode, name, quantity)
items = [
    ('100001', 'Red', 50),
    ('100002', 'Yellow', 50),
    ('100003', 'Blue', 50),
    ('100004', 'Green', 50),
]

# Connect to the database (this should be the same DB your app uses)
conn = sqlite3.connect('stock.db')
c = conn.cursor()

# Make sure table exists
c.execute('''
    CREATE TABLE IF NOT EXISTS stock (
        barcode TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

# Insert or ignore duplicates
for barcode, name, qty in items:
    c.execute('INSERT OR IGNORE INTO stock (barcode, name, quantity) VALUES (?, ?, ?)', (barcode, name, qty))

conn.commit()
conn.close()

print("✅ Items inserted into stock.db.")
