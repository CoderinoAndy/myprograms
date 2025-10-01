#Exploring SQL and investigating databases

import sqlite3
#Loads python's local SQL database system

connection = sqlite3.connect("./database.db")
#We open (would have created it if we did not download it beforehand) the existing file database.db which acts as the main database
#Returns a connection object

cursor = connection.cursor()
#Creates a cursor/access point for SQL to read the DB

query = """
SELECT * FROM products;
"""
#Select all columns from products


result = cursor.execute(query).fetchall()
#We create a result that takes the value of our cursor executing our query
#The dot fetchall pulls all result rows into a python list of tuples

print(f"OUR SQL RESULT: {result}")

connection.commit()
#Not needed for SELECT but whatever

connection.close()
#Frees resources
