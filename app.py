#for backend, we made this file
from flask import Flask,jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn=sqlite3.connect('applications.db')
    c=conn.cursor() #to run SQL commands
    c.execute("CREATE TABLE IF NOT EXISTS applications (id INTEGER PRIMARY KEY, company TEXT, role TEXT, status TEXT)")
    conn.commit()
    conn.close()
@app.route('/applications',methods=['POST'])
def add_application():
    data=request.get_json() #get data from request
    company=data['company']
    role=data['role']
    status=data['status']
    conn=sqlite3.connect('applications.db')
    c.conn.cursor()
    c.execute("INSERT INTO applications(company,role,status) VALUES(?,?,?)",(company,role,status))
    conn.commit()
    conn.close()
    return "Application added"

@app.route('/applications',methods=['GET'])
def get_applications():
    conn=sqlite3.connect('applications.db')
    c=conn.cursor()
    c.execute("SELECT * FROM applications")
    rows=c.fetchall()
    conn.close()
    app=[{"id":row[0],"company":row[1],"role":row[2],"status":row[3]} for row in rows]  
    return jsonify(app)



if __name__ == '__main__':
    init_db()
    app.run(debug=True,port=5000)