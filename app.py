import os
from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST', 'localhost')
app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER', 'chris')
app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD', 'mypassword')
app.config['MYSQL_DB'] = os.environ.get('MYSQL_DB', 'mydatabase')
app.config['MYSQL_PORT'] = int(os.environ.get('MYSQL_PORT', 3307))

mysql = MySQL(app)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/users')
def users():
    cursor = mysql.connection.cursor()
    try:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return jsonify(users)
    except Exception as e:
        return str(e)
    finally:
        cursor.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
