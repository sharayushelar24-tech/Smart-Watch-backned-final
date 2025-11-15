from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import SmartData

app = Flask(__name__)

# Database Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smartwatch.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return {"message": "Smart Watch Backend Running Successfully!"}


# Add data route
@app.route("/add_data", methods=["POST"])
def add_data():
    data = request.json
    new_entry = SmartData(
        username=data["username"],
        steps=data["steps"],
        heart_rate=data["heart_rate"],
        calories=data["calories"],
        distance=data["distance"]
    )
    db.session.add(new_entry)
    db.session.commit()

    return jsonify({"message": "Data added successfully"}), 201


# Fetch all data route
@app.route("/get_data", methods=["GET"])
def get_data():
    records = SmartData.query.all()
    output = []

    for r in records:
        output.append({
            "username": r.username,
            "steps": r.steps,
            "heart_rate": r.heart_rate,
            "calories": r.calories,
            "distance": r.distance
        })

    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)