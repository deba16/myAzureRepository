#from django.core.serializers import python
from flask import Flask, render_template
import pyodbc
from mysql.connector import errorcode
import subprocess

server = 'maximosqlserver.database.windows.net'
database = 'maximosqldb'
username = 'maximo'
password = 'wilson@123'
driver= 'SQL Server'

app = Flask(__name__,template_folder='template')
def get_data():
    try:
        conn  = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        print("Connection established")
        cursor = conn.cursor()
        # Read data
        cursor.execute("SELECT * FROM inventory;")
        rows = cursor.fetchall()
        print("Read", cursor.rowcount, "row(s) of data.")

        # Print all rows
        for row in rows:
            print("Data row = (%s, %s, %s)" % (str(row[0]), str(row[1]), str(row[2])))

        # Cleanup
        conn.commit()
        cursor.close()
        conn.close()
        print("Done.")
        return (rows)
    except:
        {
            print("Done.")
        }


@app.route('/')
def main():
   return render_template("main.html")

@app.route('/about')
def about():
    return render_template("about.html",subprocess_output=get_data())

@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)
