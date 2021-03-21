from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "account"

mysql = MySQL(app)


@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM account_details1")
    data = cur.fetchall()
    return render_template("index.html", data=data)


@app.route('/result', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        result = request.form
        number = result['number']
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT Accountnumber,Customer_name,Emailid,Balance FROM account_details1 WHERE Accountnumber='" + number + "'")
        data1 = cur.fetchall()

        return render_template("index.html", data1=data1)


@app.route('/transfer', methods=['GET', 'POST'])
def users1():
    if request.method == 'POST':
        result = request.form
        number1 = result['number1']
        number2 = result['number2']
        a = result['balance']

        cur = mysql.connection.cursor()

        cur.execute("UPDATE account_details1 SET Balance=(Balance-'" + a + "') WHERE Accountnumber= '" + number1 + "'")
        cur.execute("UPDATE account_details1 SET Balance=(Balance+'" + a + "') WHERE Accountnumber= '" + number2 + "'")
        mysql.connection.commit()

        cur.execute(
            "SELECT Accountnumber,Customer_name,Emailid,Balance FROM account_details1 ")
        data2 = cur.fetchall()

        return render_template("users.html", data2=data2)


if __name__ == "__main__":
    app.run(debug=True)
