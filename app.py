
from flask import Flask
from flask import render_template 
from flask import request
import sqlite3
app = Flask(__name__)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Function to establish connection to SQLite database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create table if not exists
def create_table():
    conn = get_db_connection()
    #c = conn.cursor()
    print("Connected to database successfully")

    conn.execute('CREATE TABLE IF NOT EXISTS patients (id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT NOT NULL UNIQUE,password TEXT NOT NULL,score TEXT NOT NULL)')
    conn.execute('CREATE TABLE IF NOT EXISTS patient_doctor (patient_id INTEGER NOT NULL,doctor_id INTEGER NOT NULL,FOREIGN KEY (patient_id) REFERENCES users (id),FOREIGN KEY (doctor_id) REFERENCES users (id))')
    conn.execute('CREATE TABLE IF NOT EXISTS visits (id INTEGER PRIMARY KEY AUTOINCREMENT,patient_id INTEGER NOT NULL,visit_date DATE NOT NULL,FOREIGN KEY (patient_id) REFERENCES users (id))')
    conn.execute('CREATE TABLE IF NOT EXISTS proteins (id INTEGER PRIMARY KEY AUTOINCREMENT,visit_id INTEGER NOT NULL,name TEXT NOT NULL,FOREIGN KEY (visit_id) REFERENCES visits (id))')
    conn.execute('CREATE TABLE IF NOT EXISTS peptides ( id INTEGER PRIMARY KEY AUTOINCREMENT, visit_id INTEGER NOT NULL, name TEXT NOT NULL,FOREIGN KEY (visit_id) REFERENCES visits (id))')

    print("Created table successfully!")
    conn.commit()
    conn.close()

# Fetch all doctors from the database
def get_patients():
    conn = get_db_connection()
    patients = conn.execute('SELECT * FROM patients').fetchall()
    conn.close()
    return patients

""" # Home Page route
@app.route("/",  methods=['GET', 'POST'])
def login():
    return render_template( "login.html") """

@app.route("/")
def home():

    return render_template( "home.html")


if __name__ == '__main__':
    app.run(debug=True)