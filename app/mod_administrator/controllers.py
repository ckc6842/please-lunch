# Import flask dependencies
from flask import Blueprint, render_template, request, jsonify
from app import app, db
from app.models import Food, Cook, Taste, Nation


mod_administrator = Blueprint('administrator', __name__, url_prefix='/admin')


@mod_administrator.route('/food', methods=['GET', 'POST'])
def administrator():
    print "start"
    return render_template("administrator/sb-admin/pages/index.html")


@mod_administrator.route('/food/add', methods=['GET', 'POST'])
def addfood():
    if request.method == 'POST':
        print request.get_data()
        temp = Food(request.json['foodName'])
        db.session.add(temp)
        db.session.commit()
    return 'seccess'


@mod_administrator.route('/food/delete', methods=['GET', 'POST'])
def deletefood():
    if request.method == 'POST':
        print request.get_data()
        temp = Food(request.json['foodName'])
        Food.query.filter_by(foodName=temp.foodName).delete()
        db.session.commit()
    return 'seccess'


@mod_administrator.route('/food/dataget', methods=['GET'])
def dataget():
    data = Food.query.all()
    return jsonify({'food': [{'foodName': item.foodName, 'id': item.id} for item in data]})

