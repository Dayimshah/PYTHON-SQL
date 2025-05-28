import mysql.connector

# Step 1: Connect to MySQL server (without selecting DB initially)
mydb = mysql.connector.connect(
    host='badguest',
    user='youduh',
    password='youknowik'
)
cur = mydb.cursor()

# Step 2: Create database if it doesn't exist
cur.execute("CREATE DATABASE IF NOT EXISTS inventory_management")

# Step 3: Connect to the inventory_management database
mydb = mysql.connector.connect(
    host='localfound',
    user='leaf',
    password='blabberuseyourownpassword',
    database='yourwish'
)
print("Connection ID:", mydb.connection_id)
cur = mydb.cursor()

# Step 4: Create tables
cur.execute('''
    CREATE TABLE IF NOT EXISTS manufacture (
        manufacture_id INT,
        item VARCHAR(30),
        no_of_items_required INT,
        defective INT
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS goods (
        goods_id INT,
        item VARCHAR(30),
        company VARCHAR(30),
        manufacture_date DATE
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS purchase (
        store_type VARCHAR(30),
        purchase_id INT,
        purchase_amount INT,
        items VARCHAR(30)
    )
''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS sale (
        store VARCHAR(30),
        sale_date DATE,
        profit_margin FLOAT,
        salesitem VARCHAR(30)
    )
''')

# Step 5: Insert data
# Manufacture
a = 'INSERT INTO manufacture (manufacture_id, item, no_of_items_required, defective) VALUES (%s, %s, %s, %s)'
z = [
    (200, 'wooden table', 2, 0),
    (201, 'wooden chair', 1, 0),
    (202, 'red coloured toys', 3, 0),
    (204, 'shirt', 2, 1)
]
cur.executemany(a, z)
mydb.commit()

# Goods
a = 'INSERT INTO goods (goods_id, item, company, manufacture_date) VALUES (%s, %s, %s, %s)'
z = [
    (300, 'wooden table', 'ss export company', '2023-04-01'),
    (301, 'wooden chair', 'abd company', '2023-04-29'),
    (302, 'red coloured toys', 'xyz company', '2023-05-01'),
    (304, 'shirt', 'bc company', '2023-05-01')
]
cur.executemany(a, z)
mydb.commit()

# Purchase
a = 'INSERT INTO purchase (store_type, purchase_id, purchase_amount, items) VALUES (%s, %s, %s, %s)'
z = [
    ('offline', 400, 56000, 'wooden table'),
    ('online', 401, 60000, 'wooden chair'),
    ('online', 402, 10000, 'red coloured toys'),
    ('online', 403, 500, 'shirt')
]
cur.executemany(a, z)
mydb.commit()

# Sale
a = 'INSERT INTO sale (store, sale_date, profit_margin, salesitem) VALUES (%s, %s, %s, %s)'
z = [
    ('mycar store', '2023-04-02', 0.2, 'wooden table'),
    ('ab store', '2023-05-02', 0.1, 'wooden chair'),
    ('MYKIDS store', '2023-05-02', 0.1, 'red coloured toys'),
    ('Oray store', '2023-05-02', 0.1, 'shirt')
]
cur.executemany(a, z)
mydb.commit()

# Step 6: Delete defective items
a = 'DELETE FROM manufacture WHERE defective = 1'
cur.execute(a)
mydb.commit()

# Step 7: Update manufacture_id based on join with sale
a = '''
UPDATE manufacture
JOIN sale ON manufacture.item = sale.salesitem
SET manufacture.manufacture_id = 700
WHERE sale.store = 'MYKIDS store'
'''
cur.execute(a)
mydb.commit()

# Step 8: Query for items like 'wooden chair' manufactured before 2023-05-01
a = '''
SELECT item 
FROM goods 
WHERE item LIKE "%wooden chair%" AND manufacture_date < "2023-05-01"
'''
cur.execute(a)
display = cur.fetchall()
print("Items like 'wooden chair' manufactured before 2023-05-01:")
for x in display:
    print(x)

# Step 9: Query for profit margin
a = '''
SELECT sale.profit_margin 
FROM goods 
INNER JOIN sale ON sale.salesitem = goods.item 
WHERE sale.store = 'mycar store' AND goods.company = 'ss export company'
'''
cur.execute(a)
display = cur.fetchall()
print("Profit margin for mycar store and ss export company:")
print(display)
