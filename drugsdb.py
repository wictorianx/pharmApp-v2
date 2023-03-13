import sqlite3
#account_id(drug_name,drug_id,closest_to_spoil) 
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS drugs(drug_name, drug_price, drug_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)")
#cur.execute("INSERT INTO drugs(drug_name, drug_price) VALUES (?,?)",("Parol", 50))
#con.commit()
x= cur.execute("SELECT * FROM drugs ").fetchall()
print(x)