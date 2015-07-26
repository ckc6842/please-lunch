# Import flask dependencies
from flask import Blueprint, render_template, request
from app import app, db
from app.models import Food


# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_administrator = Blueprint('administrator', __name__)

# Set the route and accepted methods
@mod_administrator.route('/admin/', methods=['GET', 'POST'])
def administrator():
    if request.method == 'POST':
        print request.get_data()
        food = Food(request.json['foodName'])
        db.session.add(food)
        db.session.commit()
        return "GOOD"

    food = Food.query.all()
    return render_template("administrator/admin.html", default=food)
