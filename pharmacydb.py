import sqlite3
#account_id(drug_name,drug_id,closest_to_spoil) 
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS pharmacies(drug_id, drug_spoil_date, drug_amount, user_id, record_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)")
cur.execute("INSERT INTO pharmacies (drug_id, drug_spoil_date, drug_amount, user_id) VALUES (?,?,?,?)",(1, "23.7.2023",5,1))
con.commit()
x= cur.execute("SELECT * FROM pharmacies ").fetchall()
print(x)