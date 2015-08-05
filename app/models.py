from app import db, app
from flask.ext.security import UserMixin, RoleMixin
from flask_babel import gettext as _
from flask import current_app
from flask.ext.social import Social
from flask.ext.social.datastore import SQLAlchemyConnectionDatastore
from flask_security import Security, SQLAlchemyUserDatastore
import logging
import datetime


roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# Define a User model
class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # User Name
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))

    # Identification Data: email & password
    email    = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Authoridbtion Data: role & status
    active = db.Column(db.Boolean())
    roles  = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    login = db.Column(db.String(250), unique=True)
    confirmed_at = db.Column(db.DateTime())
    is_admin = db.Column(db.Boolean)

    @property
    def cn(self):
        if not self.first_name or not self.last_name:
            return self.email
        return u"{} {}".format(self.first_name, self.last_name)

    @classmethod
    def by_email(cls, email):
        return cls.query().filter(cls.email == email).get()

    @property
    def gravatar(self):
        email = self.email.strip()
        if isinstance(email, unicode):
            email = email.encode("utf-8")
        import hashlib
        encoded = hashlib.md5(email).hexdigest()
        return "https://secure.gravatar.com/avatar/%s.png" % encoded

    def social_connections(self):
        return Connection.query.filter(Connection.user_id == self.id).all()


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", foreign_keys=user_id, backref=db.backref('connections', order_by=id))
    provider = db.Column(db.String(255))
    profile_id = db.Column(db.String(255))
    username = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    cn = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))
    provider_id = db.Column(db.String(255))
    provider_user_id = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    rank = db.Column(db.Integer)

    def get_user(self):
        return self.user

    @classmethod
    def by_profile(cls, profile):
        provider = profile.data["provider"]
        return cls.query.filter(cls.provider == provider, cls.profile_id == profile.id).first()

    @classmethod
    def from_profile(cls, user, profile):
        if not user or user.is_anonymous():
            email = profile.data.get("email")
            if not email:
                msg = "Cannot create new user, authentication provider did not not provide email"
                logging.warning(msg)
                raise Exception(_(msg))
            conflict = User.query.filter(User.email == email).first()
            if conflict:
                msg = "Cannot create new user, email {} is already used. Login and then connect external profile."
                msg = _(msg).format(email)
                logging.warning(msg)
                raise Exception(msg)

            now = datetime.now()
            user = User(
                email=email,
                first_name=profile.data.get("first_name"),
                last_name=profile.data.get("last_name"),
                confirmed_at=now,
                active=True,
            )
            db.session.add(user)
            db.session.flush()

        assert user.id, "User does not have an id"
        connection = cls(user_id=user.id, **profile.data)
        db.session.add(connection)
        db.session.commit()
        return connection


# Define a Role model
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


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


def load_user(user_id):
    return User.query.get(user_id)


#def send_mail(msg):
#    logging.debug("msg: %s" % msg)
#    mail = current_app.extensions.get('mail')
#    mail.send(msg)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
social = Social(app, SQLAlchemyConnectionDatastore(db, Connection))
