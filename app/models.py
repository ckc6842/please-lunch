from app import db, app
from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(),
                                           onupdate=db.func.current_timestamp())


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('auth_user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# Define a User model
class User(Base, UserMixin):

    __tablename__ = 'auth_user'

    # User Name
    name    = db.Column(db.String(128),  nullable=False)

    # Identification Data: email & password
    email    = db.Column(db.String(128),  nullable=False,
                                            unique=True)
    password = db.Column(db.String(192),  nullable=False)
    active = db.Column(db.Boolean())
    # Authorisation Data: role & status
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    #old role
    #role     = db.Column(db.SmallInteger, nullable=False)
    status   = db.Column(db.SmallInteger, nullable=False)

    # New instance instantiation procedure
    """
    def __init__(self, name, email, password):
        self.name     = name
        self.email    = email
        self.password = password
    """

    def __repr__(self):
        return '<User %r>' % (self.name)


# Define a Role model
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

# Saved with facebook connection data
class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    rank = db.Column(db.Integer)



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

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))
