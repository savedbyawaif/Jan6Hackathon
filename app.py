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

@app.route("/home")
def home():     
    return render_template('index.html')

@app.route("/search")
def search():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Pharmacy")
    companyDetails = cur.fetchall()
    cur.close()
    return render_template('search.html', companyDetails = companyDetails)

@app.route("/companies")
def users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM Pharmacy")
    companyDetails = cur.fetchall()
    cur.close()
    return render_template('companies.html', companyDetails = companyDetails)

@app.route("/pharmacy", methods=['GET'])
def pharmacy():
    cur = mysql.connection.cursor()
    company_name = request.args.get('company_name')
    cur.execute("SELECT * FROM Pharmacy WHERE company_name = %s", (company_name,))
    companyDetails = cur.fetchall()
    return render_template('companies.html', companyDetails = companyDetails)

@app.route("/services", methods=['GET'])
def services():
    cur = mysql.connection.cursor()
    company_name = request.args.get('company_name')
    cur.execute("SELECT * FROM Pharmacy WHERE company_name = %s", (company_name,))
    companyDetails = cur.fetchall()
    return render_template('services.html', companyDetails = companyDetails)

@app.route("/results")
def results():
    service = request.args.get('service')
    cur = mysql.connection.cursor()
    cur.execute(f"SELECT * FROM Pharmacy WHERE {service} IS NOT NULL")
    companyDetails = cur.fetchall()
    cur.close()
    return render_template('results.html', companyDetails = companyDetails, service = service)
    
if __name__ == "__main__":
    app.run(debug=True)