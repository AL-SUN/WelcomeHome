from flask import Blueprint, request, jsonify, session, redirect, url_for, flash
import mysql.connector
import hashlib
import os
import base64
from utils import get_db_connection  # Assuming your connection class is in db_connection.py
from flask_cors import cross_origin

from werkzeug.security import check_password_hash, generate_password_hash


auth_bp = Blueprint('auth_bp', __name__)

def hash_password(password):
    salt = os.urandom(16)  # Generate a random salt
    salted_password = salt + password.encode('utf-8')
    hashed_password = hashlib.sha256(salted_password).hexdigest()
    return base64.b64encode(salt + hashed_password.encode('utf-8'))  # Store salt with the hash

def check_password(stored_encoded_password, provided_password):
    stored_password = base64.b64decode(stored_encoded_password)
    salt = stored_password[:16]  # Extract the salt
    salted_provided_password = salt + provided_password.encode('utf-8')
    hashed_provided_password = hashlib.sha256(salted_provided_password).hexdigest()
    return stored_password[16:] == hashed_provided_password.encode('utf-8')

@auth_bp.route('/roles', methods=['POST'])
@cross_origin()
def get_roles():
    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT roleID, rDescription FROM Role")
        roles = cursor.fetchall()

        # Prepare the response
        roles_list = [{'roleID': role[0], 'description': role[1]} for role in roles]

        return jsonify(roles_list), 200
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500
    finally:
        cursor.close()
        connection.close()

@auth_bp.route('/register', methods=['POST'])
@cross_origin()
def register():
    user_data = request.get_json()
    userName = user_data['userName']
    password = user_data['password']
    fname = user_data['fname']
    lname = user_data['lname']
    email = user_data['email']
    phones = user_data.get('phones', [])  # Expecting a list of phone numbers
    role_id = user_data.get('roleID')  # Expecting a role ID

    # Hash the password
    hashed_password = generate_password_hash(password)

    connection = get_db_connection()
    cursor = connection.cursor()

    try:
        # Insert user into Person table
        cursor.execute("INSERT INTO Person (userName, password, fname, lname, email) VALUES (%s, %s, %s, %s, %s)",
                       (userName, hashed_password, fname, lname, email))
        
        # Insert phone numbers into PersonPhone table
        for phone in phones:
            cursor.execute("INSERT INTO PersonPhone (userName, phone) VALUES (%s, %s)", (userName, phone))
        
        # Insert role into Act table
        if role_id:
            cursor.execute("INSERT INTO Act (userName, roleID) VALUES (%s, %s)", (userName, role_id))

        connection.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except mysql.connector.Error as err:
        connection.rollback()  # Rollback in case of error
        return jsonify({"error": str(err)}), 400
    finally:
        cursor.close()
        connection.close()

@auth_bp.route('/login', methods=['POST'])
@cross_origin()
def login():
    user_data = request.get_json()
    userName = user_data['userName']
    password = user_data['password']

    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Person WHERE userName = %s", (userName,))
    user = cursor.fetchone()

    # if user and check_password(user[1].encode('utf-8'), password):
    if user and check_password_hash(user[1], password):
        session['userName'] = user[0]  # Store username in session
        session['fname'] = user[2]
        session['lname'] = user[3]
        return jsonify({"message": "Login success!"}), 200
    else:
        flash("Login failed: Invalid username or password.")
        return jsonify({"error": "Invalid username or password"}), 401

@auth_bp.route('/protected', methods=['GET'])
@cross_origin()
def protected_resource(): # test protected
    if 'userName' in session:
        return f"Welcome to the protected resource, {session['fname']} {session['lname']}!"
    return jsonify({"error": "Please login first"}), 401