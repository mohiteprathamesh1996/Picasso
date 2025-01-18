# backend/models/review.py
from app import db

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photographer_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    client_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500))

    def __repr__(self):
        return f'<Review by {self.client_id} for {self.photographer_id}>'
