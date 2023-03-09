from hashlib import sha256
import sqlite3

def encrypt(x):
    return sha256(x.encode('utf-8')).hexdigest()
con = sqlite3.connect("database.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS accounts(encrypted_username, encrypted_password, user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL)")
cur.execute("INSERT INTO accounts (encrypted_username, encrypted_password) VALUES (?,?)",(encrypt("12345678910"),encrypt("123abc..")))
con.commit()
x= cur.execute("SELECT * FROM accounts ").fetchall()
print(x)