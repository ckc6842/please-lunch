# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a User model

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodName = db.Column(db.String(128))
    foodscore = db.relationship('FoodScore', backref='food', lazy='dynamic')

    def __init__(self, foodName):
        self.foodName = foodName

    def __repr__(self):
        return '<foodName %r>' % self.foodName

class Cook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cookName = db.Column(db.String(128))

    def __init__(self, cookName):
        self.cookName = cookName

    def __repr__(self):
        return '<Cook %r>' % self.cookName

class Taste(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tasteName = db.Column(db.String(128))

    def __init__(self, tasteName):
        self.tasteName = tasteName

    def __repr__(self):
        return '<Taste %r>' % self.tasteName

class Nation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nationName = db.Column(db.String(128))

    def __init__(self, nationName):
        self.nationName = nationName

    def __repr__(self):
        return '<Nation %r>' % self.nationName

class Time(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timeName = db.Column(db.String(128))
    startTime = db.Column(db.Integer)

    def __init__(self, timeName, startTime):
        self.timeName = timeName
        self.startTime = startTime

    def __repr__(self):
        return '<Time %r>' % self.timeName

class FoodScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    EnumSet = (EnumSet_Food, EnumSet_Cook, EnumSet_Taste, EnumSet_Nation) = ('Food', 'Cook', 'Taste', 'Nation')
    targetEnum = db.Column(db.Enum(*EnumSet))
    targetId = db.Integer
    score = db.Integer
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))

    def __init__(self, EnumSet, targetEnum, targetId, score):
        self.EnumSet = EnumSet
        self.targetEnum = targetEnum
        self.targetId = targetId
        self.score = score

    def __repr__(self):
        return '<score %r>' % self.score