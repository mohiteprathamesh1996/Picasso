# backend/routes/auth.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

auth_bp = Blueprint('auth', __name__)

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photographers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database and migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Signup Route
@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    # Perform validation (ensure data contains necessary fields)
    # Create user logic here (e.g., saving user to the database)

    with app.app_context():
        db.create_all()
        print("Tables:", db.metadata.tables)
        new_user = User(
            id = data["id"],
            username = data['username'], 
            email = data["email"],
            password = data['password'],
            role = data["role"]
            )
        db.session.add(new_user)
        db.session.commit()

    # Verify user is added
    # users = User.query.all()
    # print(users)
    
    return jsonify(message="User created successfully"), 201

# Login Route
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    # Find the user based on the username
    user = User.query.filter_by(username=data['username']).first()
    
    if user and user.check_password(data['password']):  # Assuming check_password exists
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Invalid credentials"), 401
