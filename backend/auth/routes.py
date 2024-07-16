from flask import jsonify, request, session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

from auth import auth_bp
from models import Users


@auth_bp.route('/register', methods=['POST'])
def register():
    """REGISTER NEW USER ROUTE"""

    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    if not username or not password or not email:
        return jsonify({'message': 'Username and password required!'}), 400
    
    # check if username exists. Must be unique
    existing_user = Users.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already exists!'}), 400
    
    hashed_pwd = generate_password_hash(password, method='pbkdf2:sha256:20000')
    new_user = Users(username=username, email=email, password_hash=hashed_pwd)

    new_user.save()

    return jsonify({'message': 'User registered successfully!'}), 201



@auth_bp.route('/login', methods=['POST'])
def login():
    """LOGIN ROUTE"""
    username = request.json.get('username')
    password = request.json.get('password')

    if not username or not password:
        return jsonify({'error':'Missing username or password!'}), 400

    user = Users.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Invalid Credentials!'}), 401
    
    login_user(user)
    print('current user: ', current_user)
    print('authenticated?: ', current_user.is_authenticated)

    return jsonify({'message':'Logged in successfully'}), 200


@auth_bp.route('/', methods=['GET'])
@login_required
def test_protected_route():
    """TEST AUTHENTICATION ROUTE. TODO: REMOVE LATER"""
    return 'hello'


@auth_bp.route('/logout')
@login_required
def logout():
    """LOGOUT ROUTE"""
    logout_user()
    print('current user: ', current_user)
    print('authenticated?: ', current_user.is_authenticated)

    return jsonify({'message': 'Logged out successfully'}), 200
