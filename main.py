# import sqlite3
#
# def create():
#     conn = sqlite3.connect("example.db")
#     cursor = conn.cursor()
#
#     cursor.execute("""CREATE TABLE users
#         (id INT PRIMARY KEY, name TEXT, email TEXT)
#     """)
#     conn.close()
#
#
# def add():
#     conn = sqlite3.connect("example.db")
#     cursor = conn.cursor()
#
#     name = input("name: ")
#     email = input("email: ")
#
#     cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
#     conn.commit()
#     conn.close()
#
#
# def get_data():
#     conn = sqlite3.connect("example.db")
#     cursor = conn.cursor()
#
#     cursor.execute("""SELECT * FROM users""")
#
#     result = cursor.fetchone()
#     print(result)
#     conn.close()
#
# def delete():
#     conn = sqlite3.connect("example.db")
#     cursor = conn.cursor()
#
#     id = input("id: ")
#     cursor.execute("DELETE * FROM users WHERE name = ?", id)
#     conn.commit()
#     conn.close()
#
#
# try:
#     create()
# except:
#     print("Already exist")
#     # add()
#     delete()
#     get_data()

import sqlite3

def create():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE products 
        (id INT PRIMARY KEY,
        name TEXT,
        price REAL,
        quantity INT)
    """)
    conn.close()

def add():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    products_data = [
        (1, 'Tovar 1', 10.99, 100),
        (2, 'Tovar 2', 15.99, 50),
        (3, 'Tovar 3', 5.99, 200)
    ]
    for product in products_data:
        cursor.execute("INSERT INTO products (id, name, price, quantity) VALUES (?, ?, ?, ?)", product)
    conn.commit()
    conn.close()

def get_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    result = cursor.fetchall()
    print(result)
    conn.close()

try:
    create()
except:
    print("Already exist")
    # add()
    get_db()
