from app import db, app
from flask.ext.security import UserMixin, RoleMixin
from flask_babel import gettext as _
from flask_security import Security, SQLAlchemyUserDatastore
from flask_security.utils import encrypt_password
import logging
import datetime


roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


def password_generator(length):
    import random

    alphabet = "abcdefghijklmnopqrstuvwxyz~!@#$%^&*()-_|+=/.,<>'"
    pw_length = length
    mypw = ""

    for i in range(pw_length):
        next_index = random.randrange(len(alphabet))
        mypw = mypw + alphabet[next_index]

    # replace 1 or 2 characters with a number
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2)
        mypw = mypw[0:replace_index] + str(random.randrange(10)) + mypw[replace_index+1:]

    # replace 1 or 2 letters with an uppercase letter
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(mypw)//2,len(mypw))
        mypw = mypw[0:replace_index] + mypw[replace_index].upper() + mypw[replace_index+1:]

    return mypw


# Define a User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    # for foreign key
    user_score = db.relationship("UserScore", backref=db.backref('user'))
    user_food = db.relationship("UserFood", backref=db.backref('user'))
    user_food_score = db.relationship("UserFoodScore", backref=db.backref('user'))


    # User Name
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))

    # Identification Data: email & password
    email    = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # Auth Data: role & status
    active = db.Column(db.Boolean(), default=False)
    roles  = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))

    # for checking user's food evaluation
    is_evaluate = db.Column(db.Boolean(), default=False)

    # for checking user want to leave the site
    is_want_leave = db.Column(db.Boolean(), default=False)

    # for SECURITY_TRACKABLE and CONFIRMABLE
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(25))
    current_login_ip = db.Column(db.String(25))
    login_count = db.Column(db.Integer())

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

    def get_facebook_connections(self):
        return Connection.query.filter(Connection.provider == 'Facebook', Connection.user_id == self.id).all()


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", foreign_keys=user_id, backref=db.backref('connections', order_by=id))
    provider = db.Column(db.String(255))
    profile_id = db.Column(db.String(255))
    email = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    username = db.Column(db.String(255))
    full_name = db.Column(db.String(255))
    access_token = db.Column(db.String(255))
    secret = db.Column(db.String(255))
    cn = db.Column(db.String(255))
    profile_url = db.Column(db.String(512))
    image_url = db.Column(db.String(512))

    def get_user(self):
        return self.user

    @classmethod
    def by_profile(cls, profile):
        provider = profile.data["provider"]
        return cls.query.filter(cls.provider == provider, cls.profile_id == profile.id).first()

    @classmethod
    def from_profile(cls, user, profile):
        provider = profile.data["provider"]
	
        if not user or user.is_anonymous():
            # twiiter does not provide email
            if not provider == 'Twitter':
                email = profile.data.get("email")
                if not email:
                    msg = "Cannot create new user, authentication provider did not provide email"
                    logging.warning(msg)
                    raise Exception(_(msg))
                conflict = User.query.filter(User.email == email).first()
                if conflict:
                    msg = "Cannot create new user, email {} is already used. Login and then connect external profile."
                    msg = _(msg).format(email)
                    logging.warning(msg)
                    raise Exception(msg)
            else:
                username = profile.data.get("username")
		email = username + "@" + "fox.net"

            now = datetime.datetime.now()
            password = password_generator(16)
            user = User(
                email=email,
                password=encrypt_password(password),
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
    foodscore = db.relationship("FoodScore", backref=db.backref('food'))
    user_food = db.relationship("UserFood", backref=db.backref('food'))
    user_food_score = db.relationship("UserFoodScore", backref=db.backref('food'))

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
    user_food = db.relationship("UserFood", backref=db.backref('time'))

    def __init__(self, timeName, startTime):
        self.timeName = timeName
        self.startTime = startTime

    def __repr__(self):
        return '<Time %r>' % self.timeName


class FoodScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    EnumSet = ['Cook', 'Taste', 'Nation']
    targetEnum = db.Column(db.Enum(*EnumSet))
    targetId = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, food, targetEnum, targetId, score):
        self.food = food
        self.targetEnum = targetEnum
        self.targetId = targetId
        self.score = score

    def __repr__(self):
        return '<FoodScore %r>' % self.score


class UserScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    EnumSet = ['Cook', 'Taste', 'Nation']
    targetEnum = db.Column(db.Enum(*EnumSet))
    targetId = db.Column(db.Integer)
    score = db.Column(db.Integer)

    def __init__(self, user_id, targetEnum, targetId, score):
        self.user_id = user_id
        self.targetEnum = targetEnum
        self.targetId = targetId
        self.score = score

    def __repr__(self):
        return '<UserScore %r>' % self.score


class UserFood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    time_id = db.Column(db.Integer, db.ForeignKey('time.id'))

    def __init__(self, user_id, food_id, time_id):
        self.user_id = user_id
        self.food_id = food_id
        self.time_id = time_id

    def __repr__(self):
        return '<UserFood user_id : %r food_id : %r time_id : %r>' % (self.user_id, self.food_id, self.time)


class UserFoodScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    food_id = db.Column(db.Integer, db.ForeignKey('food.id'))
    score = db.Column(db.Integer)

    def __init__(self, user_id, food_id, score):
        self.user_id = user_id
        self.food_id = food_id
        self.score = score

    def __repr__(self):
        return '<UserFoodScore user_id : %r food_id : %r score : %r>' % (self.user_id, self.food_id, self.score)


def load_user(user_id):
    return User.query.get(user_id)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

from flask_social_blueprint.core import SocialBlueprint
SocialBlueprint.init_bp(app, Connection, url_prefix="/_social")




