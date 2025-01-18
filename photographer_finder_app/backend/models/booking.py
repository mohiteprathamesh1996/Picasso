# backend/models/booking.py
from app import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    photographer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(10), default='pending')

    def __repr__(self):
        return f'<Booking {self.id} for {self.client_id} with {self.photographer_id}>'
