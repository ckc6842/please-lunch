# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, jsonify
from flask.ext.login import login_required
from flask_security import roles_required

from app import db
from app.models import Food, Cook, Taste, Nation, FoodScore


mod_administrator = Blueprint('admin', __name__, url_prefix='/admin')


@roles_required('admin')
@login_required
@mod_administrator.route('/index/', methods=['GET'])
def index():
    return render_template("administrator/sb-admin/pages/index.html")


@roles_required('admin')
@login_required
@mod_administrator.route('/getdata', methods=['GET'])
def getdata():
    food_data = Food.query.all()
    cook_data = Cook.query.all()
    nation_data = Nation.query.all()
    taste_data = Taste.query.all()

    return jsonify({'food': [{'foodName': item.foodName, 'id': item.id} for item in food_data],
                    'cook': [{'cookName': item.cookName, 'id': item.id} for item in cook_data],
                    'nation': [{'nationName': item.nationName, 'id': item.id} for item in nation_data],
                    'taste': [{'tasteName': item.tasteName, 'id': item.id} for item in taste_data]})


@roles_required('admin')
@login_required
@mod_administrator.route('/foodscore/<foodName>', methods=['GET', 'POST'])
def foodscore(foodName):

    if request.method == 'POST':

        food_temp = Food.query.filter_by(foodName = foodName).first()

        for i in request.json['cookName']:
            cook_temp = Cook.query.filter_by(cookName=i).first()
            if FoodScore.query.filter(FoodScore.food_id == food_temp.id).filter(FoodScore.targetEnum == 'Cook').filter(FoodScore.targetId == cook_temp.id).count() == 0:
                db.session.add(FoodScore(food_temp, 'Cook', cook_temp.id, 1))
            else:
                pass
        for i in request.json['nationName']:
            nation_temp = Nation.query.filter_by(nationName=i).first()
            if FoodScore.query.filter(FoodScore.food_id == food_temp.id).filter(FoodScore.targetEnum == 'Nation').filter(FoodScore.targetId == nation_temp.id).count() == 0:
                db.session.add(FoodScore(food_temp, 'Nation', nation_temp.id, 1))
            else:
                pass

        for i in request.json['tasteScore']:
            taste_temp = Taste.query.filter_by(tasteName=i['tasteName']).first()
            if FoodScore.query.filter(FoodScore.food_id == food_temp.id).filter(FoodScore.targetEnum == 'Taste').filter(FoodScore.targetId == taste_temp.id).count() == 0:
                db.session.add(FoodScore(food_temp, 'Taste', taste_temp.id, i['score']))
            else:
                pass

        db.session.commit()

        return 'succes'

    return render_template("administrator/sb-admin/pages/food-score.html")


# foodscore
@roles_required('admin')
@login_required
@mod_administrator.route('/foodscore/', methods=['GET', 'POST'])
def foodscore_index():
    if request.method == 'POST':
        food_id = Food.query.filter_by(foodName = request.json['foodName'] ).one().id
        temp = FoodScore.query.filter(FoodScore.food_id == food_id).filter(FoodScore.targetEnum == request.json['targetEnum']).filter(FoodScore.targetId == request.json['targetId']).one()
        temp.score = request.json['score']
        db.session.add(temp)
        db.session.commit()

        return 'good'

    return render_template("administrator/sb-admin/pages/food-score-table.html")


@roles_required('admin')
@login_required
@mod_administrator.route('/foodscore/delete/', methods=['GET', 'POST'])
def foodscore_delete():
    food_id = Food.query.filter_by(foodName = request.json['foodName'] ).one().id
    FoodScore.query.filter(FoodScore.food_id == food_id).filter(FoodScore.targetEnum == request.json['targetEnum']).filter(FoodScore.targetId == request.json['targetId']).delete()
    db.session.commit()
    return 'good'


@roles_required('admin')
@login_required
@mod_administrator.route('/test/', methods=['GET', 'POST'])
def test():
    p = FoodScore.query.filter(FoodScore.food_id == 1)
    print p
    return 'good'


@roles_required('admin')
@login_required
@mod_administrator.route('/foodscore/getdata/', methods=['GET'])
def get_foodscore():
    foodscore_cook_table = db.session.query(FoodScore, Cook).outerjoin(Cook, FoodScore.targetId == Cook.id).filter(FoodScore.targetEnum == 'Cook')
    foodscore_taste_table = db.session.query(FoodScore, Taste).outerjoin(Taste, FoodScore.targetId == Taste.id).filter(FoodScore.targetEnum == 'Taste')
    foodscore_nation_table = db.session.query(FoodScore, Nation).outerjoin(Nation, FoodScore.targetId == Nation.id).filter(FoodScore.targetEnum == 'Nation')

    return jsonify({'foodscore_cook': [{'food_id': item[0].food_id, 'id': item[0].id, 'foodName' : item[0].food.foodName,
                                   'targetName': item[1].cookName, 'targetId': item[0].targetId, 'targetEnum' : item[0].targetEnum, 'score' : item[0].score } for item in foodscore_cook_table],
                   'foodscore_taste': [{'food_id': item[0].food_id, 'id': item[0].id, 'foodName' : item[0].food.foodName,
                                   'targetName': item[1].tasteName, 'targetId': item[0].targetId, 'targetEnum' : item[0].targetEnum, 'score' : item[0].score } for item in foodscore_taste_table],
                   'foodscore_nation': [{'food_id': item[0].food_id, 'id': item[0].id, 'foodName' : item[0].food.foodName,
                                   'targetName': item[1].nationName, 'targetId': item[0].targetId, 'targetEnum' : item[0].targetEnum, 'score' : item[0].score } for item in foodscore_nation_table]}
    )


# food
@roles_required('admin')
@login_required
@mod_administrator.route('/food', methods=['GET'])
def food_index():
    print "food start"
    return render_template("administrator/sb-admin/pages/food.html")


@roles_required('admin')
@login_required
@mod_administrator.route('/food/add', methods=['GET', 'POST'])
@login_required
def addfood():
    print 'add'
    if request.method == 'POST':
        print request.get_data()
        temp = Food(request.json['foodName'])
        db.session.add(temp)
        db.session.commit()
    return 'seccess'


@roles_required('admin')
@login_required
@mod_administrator.route('/food/delete', methods=['GET', 'POST'])
@login_required
def deletefood():
    if request.method == 'POST':
        print request.get_data()
        temp = Food(request.json['foodName'])
        Food.query.filter_by(foodName=temp.foodName).delete()
        db.session.commit()
    return 'seccess'

#

@roles_required('admin')
@login_required
@mod_administrator.route('/cook', methods=['GET'])
def cook_index():
    print "cook start"
    return render_template("administrator/sb-admin/pages/cook.html")


@roles_required('admin')
@login_required
@mod_administrator.route('/cook/add', methods=['GET', 'POST'])
def addcook():
    if request.method == 'POST':
        print request.get_data()
        temp = Cook(request.json['cookName'])
        db.session.add(temp)
        db.session.commit()
    return 'seccess'


@roles_required('admin')
@login_required
@mod_administrator.route('/cook/delete', methods=['GET', 'POST'])
def deletecook():
    if request.method == 'POST':
        print request.get_data()
        temp = Cook(request.json['cookName'])
        Cook.query.filter_by(cookName=temp.cookName).delete()
        db.session.commit()
    return 'seccess'


# nation
@roles_required('admin')
@login_required
@mod_administrator.route('/nation', methods=['GET'])
def nation_index():
    print "nation start"
    return render_template("administrator/sb-admin/pages/nation.html")


@roles_required('admin')
@login_required
@mod_administrator.route('/nation/add', methods=['GET', 'POST'])
def addnation():
    if request.method == 'POST':
        print request.get_data()
        temp = Nation(request.json['nationName'])
        db.session.add(temp)
        db.session.commit()
    return 'seccess'


@roles_required('admin')
@login_required
@mod_administrator.route('/nation/delete', methods=['GET', 'POST'])
def deletenation():
    if request.method == 'POST':
        print request.get_data()
        temp = Nation(request.json['nationName'])
        Nation.query.filter_by(nationName=temp.nationName).delete()
        db.session.commit()
    return 'seccess'


# taste
@roles_required('admin')
@login_required
@mod_administrator.route('/taste', methods=['GET'])
def taste_index():
    print "taste start"
    return render_template("administrator/sb-admin/pages/taste.html")


@roles_required('admin')
@login_required
@mod_administrator.route('/taste/add', methods=['GET', 'POST'])
def addtaste():
    if request.method == 'POST':
        print request.get_data()
        temp = Taste(request.json['tasteName'])
        db.session.add(temp)
        db.session.commit()
    return 'seccess'


@roles_required('admin')
@login_required
@mod_administrator.route('/taste/delete', methods=['GET', 'POST'])
def deletetaste():
    if request.method == 'POST':
        print request.get_data()
        temp = Taste(request.json['tasteName'])
        Taste.query.filter_by(tasteName=temp.tasteName).delete()
        db.session.commit()
    return 'seccess'
