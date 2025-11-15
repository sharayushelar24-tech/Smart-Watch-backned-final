from db import db

class SmartData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    steps = db.Column(db.Integer, nullable=False)
    heart_rate = db.Column(db.Integer, nullable=False)
    calories = db.Column(db.Integer, nullable=False)
    distance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<SmartData {self.username}>"