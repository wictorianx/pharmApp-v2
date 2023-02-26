import sqlite3
from datetime import date
curdate = date.today()
#account_id(drug_name,drug_id,closest_to_spoil) 
con = sqlite3.connect("database.db")
cur = con.cursor()
#cur.execute("DROP TABLE sales")
cur.execute("CREATE TABLE IF NOT EXISTS sales(date, drug_id, user_id, sale_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)")
#cur.execute("INSERT INTO sales(date, drug_id, user_id) VALUES (?,?,?)",(curdate, 1,1))
con.commit()
x= cur.execute("SELECT * FROM sales ").fetchall()
print(x)