# backend/routes/bookings.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.booking import Booking, db
from models.user import User

bookings_bp = Blueprint('bookings', __name__)

@bookings_bp.route('/book', methods=['POST'])
@jwt_required()
def create_booking():
    current_user = get_jwt_identity()  # Get current user from JWT
    data = request.get_json()
    photographer = User.query.get(data['photographer_id'])
    if photographer:
        new_booking = Booking(
            client_id=current_user, 
            photographer_id=data['photographer_id'], 
            time=data['time'], 
            status='pending'
            )
        db.session.add(new_booking)
        db.session.commit()
        return jsonify({"message": "Booking created successfully!"}), 201
    return jsonify({"message": "Photographer not found"}), 400
