import pandas as pd
import sqlite3
def dumpsales(db,date,amount,drug_id,user_id):
    con = sqlite3.connect(db)
    cur = con.cursor()
    for i in range(amount):
        
        cur.execute("INSERT INTO sales(date, drug_id, user_id) VALUES (?,?,?)",(str(date)[:10], drug_id,user_id))
    con.commit()
def readExcel(file,drug_id,user_id):
    spreadsheet = pd.read_excel(file)
    for i in range(len(spreadsheet["Satış Tarihi"])-1):
        date = spreadsheet["Satış Tarihi"][i]
        amount = int(spreadsheet["Miktar"][i])
        dumpsales("database.db",date,amount,drug_id,user_id)
def getData(db, user_id):
    #2022-09-29
    years = {}
    con = sqlite3.connect(db)
    cur = con.cursor()
    data = cur.execute("SELECT * FROM sales WHERE user_id = ?",(user_id,)).fetchall()
    for i in data:
        
        date = i[0].split("-")
        year = date[0]
        month = int(date[1])
        day = int(date[2])

        drug_id = i[1]
        if year not in years:
            years[year] = {drug_id:[]}
            for i in range(12):
                years[year][drug_id].append([])
        while day>len(years[year][drug_id][month-1]):
            years[year][drug_id][month -1].append(0)
        years[year][drug_id][month-1][day-1]+=1  
    return(years)
            

            
print(getData("database.db",1))
        
        

#def refactorData(): (unnecessary??)

#def predict():




