import sqlite3

#Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

#query data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

#Query certain columns
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

#Insert new Rows
new_rows = [{'cats','Cat City','2088.10.17'),
('Hens','Hen City','2088.10.17')]

cursor.excecutemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

#Query all data
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)
