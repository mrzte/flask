from flask import Flask, request, jsonify, render_template, url_for
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)

#Koneksi Database
app.config['MYSQL_USER'] = 'admin'
app.config['MYSQL_PASSWORD'] = 'toor'
app.config['MYSQL_DB'] = 'flask'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)
CORS(app)

#Router
@app.route('/api/pilar', methods=['GET'])
def get_pilar():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM `pilar` ORDER BY `pilar`.`id` ASC")
    rv = cur.fetchall()
    return jsonify(rv)

@app.route('/')
def index():
    return render_template('index.html')

#Server
if __name__ == "__main__":
    app.run(debug=True)    