from flask import Flask, render_template, request, url_for, redirect
from hashlib import sha256
import sqlite3

def encrypt(x):
    return sha256(x.encode('utf-8')).hexdigest()

con = sqlite3.connect("database.db",check_same_thread=False)
cur = con.cursor()

app = Flask(__name__)


@app.route('/', methods=['POST','GET'])
def hello():
    return "Hello, world!"
@app.route('/accountExists', methods=['POST','GET'])
def exists():
    return "An account with this uername already exists"
@app.route('/createAccount/', methods=['POST','GET'])
def cacc():
    if request.method == 'POST':
        print(765)
        username = request.form["username"]
        password = request.form["password"]
        encryptedusername = encrypt(username)
        encryptedpassword = encrypt(password)
        try:
            saved_password=cur.execute("SELECT encrypted_password FROM accounts WHERE encrypted_username = (?)",(encryptedusername,)).fetchone()[0]
            if saved_password==encryptedpassword:
                return redirect(url_for('exists'))
        except:
            n = [None,""]
            if encryptedusername not in n and encryptedpassword not in n:
                cur.execute("INSERT INTO accounts (encrypted_username, encrypted_password) VALUES (?,?)",(encryptedusername,encryptedpassword))
                con.commit()
                print("COMMITTED")
                return redirect(url_for('hello'))

            
    return render_template('register.html')

@app.route('/login/', methods=['POST','GET'])
def login():
    print(57686755)
    
    if request.method == 'POST':
        print(546)
        username = request.form["username"]
        password = request.form["password"]
        encryptedusername = encrypt(username)
        encryptedpassword = encrypt(password)
        try:
            saved_password=cur.execute("SELECT encrypted_password FROM accounts WHERE encrypted_username = (?)",(encryptedusername,)).fetchone()[0]
            if saved_password==encryptedpassword:
                user_id= cur.execute("SELECT user_id FROM accounts WHERE encrypted_username = (?)",(encryptedusername,)).fetchone()[0]
                print(cur.execute("SELECT * FROM pharmacies WHERE user_id = (?)",(user_id,)).fetchall())
                print("Apo")
                return redirect(url_for('hello'))

        except:
            pass
    return render_template('login.html')