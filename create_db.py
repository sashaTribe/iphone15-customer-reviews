
import sqlite3

conn = sqlite3.connect('apple review table')
c = conn.cursor()

c.execute('''CREATE TABLE amazon(customer_review TEXT)''')

# Apple store

