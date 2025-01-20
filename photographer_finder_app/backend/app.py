# backend/app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initialize Flask app, Database, and Migrate
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photographers.db'  # You can switch to PostgreSQL or MySQL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Example route
@app.route('/')
def home():
    return jsonify(
        message="Welcome to the Uber for Photographers app!"
        )

if __name__ == '__main__':
    app.run(debug=True)
