import sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

usertable_q = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(usertable_q)

itemtable_q = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"
cursor.execute(itemtable_q)

# cursor.execute("INSERT INTO items VALUES ('dummy', 205.49)")
connection.commit()
connection.close()