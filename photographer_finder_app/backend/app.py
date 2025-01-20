# backend/app.py
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

# Initialize database and migrate outside the app initialization
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Create a function to initialize the app
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photographers.db'  # You can switch to PostgreSQL or MySQL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'  # Change this to a secure key

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from routes.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    # Example route
    @app.route('/')
    def home():
        return jsonify(
            message="Welcome to the Uber for Photographers app!"
        )

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
