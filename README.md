# Inventory Management System (Python + MySQL)

This project is a simple Python script that connects to a MySQL database and performs basic operations such as creating tables, inserting data, updating records, deleting records, and querying data. It models an inventory management system with tables for manufacture, goods, purchase, and sale.

---

## Features

- Creates an `inventory_management` database if it doesn't exist.
- Creates tables: `manufacture`, `goods`, `purchase`, and `sale`.
- Inserts sample data into the tables.
- Deletes defective items from `manufacture`.
- Updates manufacture IDs based on sales data.
- Runs example queries to fetch specific data.

---

## Requirements

- Python 3.x
- `mysql-connector-python` package
- MySQL Server installed and running

Install the Python MySQL connector with:

```bash
pip install mysql-connector-python
