from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import mysql.connector as mysql
from flask_limiter import Limiter

app = Flask(__name__)
CORS(app, support_credentials=True)

def get_db_connection():
    return mysql.connect(host='db',
                         user='user',
                         password='password',
                         database='mydatabase',
                         auth_plugin='mysql_native_password')

@app.route("/servertest", methods=["GET"])
@cross_origin(supports_credentials=True)
def servertest():
    return jsonify({"message": 'Hello from the backend!'})

@app.route('/create_users', methods=['POST'])
def create_user():
    # Example for creating a user
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    sql = "INSERT INTO `users` (`username`, `email`, `password`) VALUES (%s, %s, %s)"
    cursor.execute(sql, (data['username'], data['email'], data['password']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify(data), 201

@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(users)


if __name__ == "__main__":
    app.run(debug=True)
