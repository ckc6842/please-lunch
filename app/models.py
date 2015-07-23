# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a User model

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodName = db.Column(db.String(128))

    def __init__(self, foodName):
        self.foodName = foodName
