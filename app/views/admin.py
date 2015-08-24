# -*- coding: utf-8 -*-
from flask import render_template, request, jsonify
from flask_security import roles_required, login_required
from flask_classy import FlaskView, route

from app import db
from app.models import Food, Cook, Taste, Nation, FoodScore, User


class AdminView(FlaskView):
    route_base = '/admin/'
    decorators = [login_required, roles_required('admin')]

    def index(self):
        return render_template("administrator/sb-admin/pages/index.html")

    def getdata(self):
        food_data = Food.query.all()
        cook_data = Cook.query.all()
        nation_data = Nation.query.all()
        taste_data = Taste.query.all()
        user_data = User.query.all()

        return jsonify({'food': [{'foodName': item.foodName, 'id': item.id} for item in food_data],
                        'cook': [{'cookName': item.cookName, 'id': item.id} for item in cook_data],
                        'nation': [{'nationName': item.nationName, 'id': item.id} for item in nation_data],
                        'taste': [{'tasteName': item.tasteName, 'id': item.id} for item in taste_data],
                        'user': [{'email': item.email, 'id': item.id} for item in user_data]})

    @route('/foodscore/<foodName>/', methods=['POST', 'GET'])
    def foodscore(self, foodName):
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
        return render_template("administrator/sb-admin/pages/food-score.html")

    @route('/foodscore/index/', methods=['POST', 'GET'])
    def foodscore_index(self):
        if request.method == 'POST':
            food_id = Food.query.filter_by(foodName = request.json['foodName'] ).one().id
            temp = FoodScore.query.filter(FoodScore.food_id == food_id).filter(FoodScore.targetEnum == request.json['targetEnum']).filter(FoodScore.targetId == request.json['targetId']).one()
            temp.score = request.json['score']
            db.session.add(temp)
            db.session.commit()
            return 'good'

        return render_template("administrator/sb-admin/pages/food-score-table.html")

    @route('/foodscore/delete/', methods=['POST', 'GET'])
    def foodscore_delete(self):
        food_id = Food.query.filter_by(foodName = request.json['foodName'] ).one().id
        FoodScore.query.filter(FoodScore.food_id == food_id).filter(FoodScore.targetEnum == request.json['targetEnum']).filter(FoodScore.targetId == request.json['targetId']).delete()
        db.session.commit()
        return 'good'

    @route('/foodscore/test/', methods=['POST', 'GET'])
    def test(self):
        p = FoodScore.query.filter(FoodScore.food_id == 1)
        print p
        return 'good'

    @route('/foodscore/getdata/', methods=['GET'])
    def get_foodscore(self):
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

    @route('/food/', methods=['GET'])
    def food_index(self):
        print "food start"
        return render_template("administrator/sb-admin/pages/food.html")

    @route('/food/add/', methods=['POST'])
    def addfood(self):
        print 'add'
        if request.method == 'POST':
            print request.get_data()
            temp = Food(request.json['foodName'])
            db.session.add(temp)
            db.session.commit()
        return 'seccess'

    @route('/food/delete/', methods=['GET', 'POST'])
    def deletefood(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Food(request.json['foodName'])
            Food.query.filter_by(foodName=temp.foodName).delete()
            db.session.commit()
        return 'seccess'

    @route('/cook/', methods=['GET'])
    def cook_index(self):
        return render_template("administrator/sb-admin/pages/cook.html")

    @route('/cook/add/', methods=['POST'])
    def addcook(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Cook(request.json['cookName'])
            db.session.add(temp)
            db.session.commit()
        return 'seccess'

    @route('/cook/delete/', methods=['POST'])
    def deletecook(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Cook(request.json['cookName'])
            Cook.query.filter_by(cookName=temp.cookName).delete()
            db.session.commit()
        return 'seccess'

    @route('/nation/', methods=['GET'])
    def nation_index(self):
        print "nation start"
        return render_template("administrator/sb-admin/pages/nation.html")

    @route('/nation/add/', methods=['POST'])
    def addnation(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Nation(request.json['nationName'])
            db.session.add(temp)
            db.session.commit()
        return 'seccess'

    @route('/nation/delete/', methods=['POST'])
    def deletenation(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Nation(request.json['nationName'])
            Nation.query.filter_by(nationName=temp.nationName).delete()
            db.session.commit()
        return 'seccess'

    @route('/taste/', methods=['GET'])
    def taste_index(self):
        return render_template("administrator/sb-admin/pages/taste.html")

    @route('/taste/add/', methods=['POST'])
    def addtaste(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Taste(request.json['tasteName'])
            db.session.add(temp)
            db.session.commit()
        return 'seccess'

    @route('/taste/delete/', methods=['POST'])
    def deletetaste(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Taste(request.json['tasteName'])
            Taste.query.filter_by(tasteName=temp.tasteName).delete()
            db.session.commit()
        return 'seccess'

    @route('/user/', methods=['GET'])
    def user_index(self):
        return render_template("administrator/sb-admin/pages/user.html")