from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql3.freesqldatabase.com'
app.config['MYSQL_USER'] = 'sql3675087'
app.config['MYSQL_PASSWORD'] = 'CaaVkk75W1'
app.config['MYSQL_DB'] = 'sql3675087'

mysql = MySQL(app)

@app.route("/",methods=['GET','POST'])
def index():     
    return render_template('index.html')

@app.route("/search")
def reg():
    return render_template('search.html')

@app.route("/companies")
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Pharmacy")
    companyDetails = cur.fetchall()
    cur.close()
    return render_template('companies.html', companyDetails = companyDetails)

if __name__ == "__main__":
    app.run(debug=True)