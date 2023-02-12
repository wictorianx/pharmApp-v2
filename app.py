from flask import Flask, render_template, request, url_for, redirect
from hashlib import sha256
import sqlite3
import pandas as pd
import pharmacy

logged_in = False
user_id = None
def encrypt(x):
    return sha256(x.encode('utf-8')).hexdigest()
con = sqlite3.connect("database.db",check_same_thread=False)
cur = con.cursor()

app = Flask(__name__)

drugs=[]
@app.route('/', methods=['POST','GET'])
def hello():
    return "Hello, world!"
@app.route('/prediction/', methods=['POST','GET'])
def predict():
    if request.method == 'POST':  
        f = request.files['file']
        filename=f.filename.split(".")[0].capitalize()
        
        id = cur.execute("SELECT drug_id FROM drugs WHERE drug_name=(?)",(filename,)).fetchone()[0]
        pharmacy.readExcel(f,id,user_id)
        print(filename)
        print(user_id)
        print(logged_in)
        
    return render_template("prediction.html")
@app.route('/mypharmacy/', methods=['POST','GET'])
def myPharmacy():
    if request.method == 'POST':  
        f = request.files['file']
        filename=f.filename.split(".")[0].capitalize()
        id = cur.execute("SELECT drug_id FROM drugs WHERE drug_name=(?)",(filename,)).fetchone()[0]
        print(id)
        #pharmacy.readExcel()
        
        
    return render_template('mypharmacy.html',drugs=drugs)
@app.route('/accountExists/', methods=['POST','GET'])
def exists():
    return "An account with this username already exists"
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
                return redirect(url_for('myPharmacy'))

            
    return render_template('register.html')
def convertDrugs(drugs):
    for i in range(len(drugs)):
        drugs[i]=list(i)

@app.route('/login/', methods=['POST','GET'])
def login():
    global drugs
    global logged_in
    global user_id
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
                logged_in = True
                user_id= cur.execute("SELECT user_id FROM accounts WHERE encrypted_username = (?)",(encryptedusername,)).fetchone()[0]
                drugs= cur.execute("SELECT * FROM pharmacies WHERE user_id = (?)",(user_id,)).fetchall()
                for i in range(len(drugs)):
                    drugs[i]=list(drugs[i])
                print(1)
                print(drugs)
                print("Apo")
                return redirect(url_for('myPharmacy'))

        except:
            pass
    return render_template('login.html')