# -*- coding: utf-8 -*-
# 관리자 페이지
from flask import render_template, request, jsonify
from flask_security import roles_required, login_required
from flask_classy import FlaskView, route

from app import db
from app.models import Food, Cook, Taste, Nation, FoodScore, User, Time


class AdminView(FlaskView):
    route_base = '/admin/'
    decorators = [login_required, roles_required('admin')]

    def index(self):
        return render_template("administrator/sb-admin/pages/index.html")

    # foodscore는 너무 길어서 따로 GET, 다른테이블의 데이터 리턴
    def getdata(self):
        food_data = Food.query.all()
        cook_data = Cook.query.all()
        nation_data = Nation.query.all()
        taste_data = Taste.query.all()
        user_data = User.query.all()
        time_data = Time.query.all()
        return jsonify(
            {
                'food':
                    [
                        {
                            'foodName': item.foodName,
                            'id': item.id
                        } for item in food_data
                    ],
                'cook':
                    [
                        {
                            'cookName': item.cookName,
                            'id': item.id
                        } for item in cook_data
                    ],
                'nation':
                    [
                        {
                            'nationName': item.nationName,
                            'id': item.id
                        } for item in nation_data
                    ],
                'taste':
                    [
                        {
                            'tasteName': item.tasteName,
                            'id': item.id
                        } for item in taste_data
                    ],
                'user':
                    [
                        {
                            'email': item.email,
                            'id': item.id
                        } for item in user_data
                    ],
                'time':
                    [
                        {
                            'timeName': item.timeName,
                            'startTime': item.startTime,
                            'id': item.id
                        } for item in time_data
                    ]
            }
        )

    # url에서 foodName을 가져와서 적절히 FoodScore테이블에 삽입
    @route('/foodscore/<foodName>/', methods=['POST', 'GET'])
    def foodscore(self, foodName):
        if request.method == 'POST':

            # url로부터 "어떤음식?"에 대한걸 결정
            food_temp = Food.query.filter_by(foodName=foodName).first()

            # FoodScore에 이미 해당 Food를 평가한 기록이 있으면 pass
            for i in request.json['cookName']:
                cook_temp = Cook.query.filter_by(cookName=i).first()
                if FoodScore.query.filter(FoodScore.food_id == food_temp.id)\
                                  .filter(FoodScore.targetEnum == 'Cook')\
                                  .filter(FoodScore.targetId == cook_temp.id)\
                                  .count() == 0:
                    db.session.add(FoodScore(food_temp, 'Cook', cook_temp.id, 1))
                else:
                    pass

            for i in request.json['nationName']:
                nation_temp = Nation.query.filter_by(nationName=i).first()
                if FoodScore.query.filter(FoodScore.food_id == food_temp.id)\
                                  .filter(FoodScore.targetEnum == 'Nation')\
                                  .filter(FoodScore.targetId == nation_temp.id)\
                                  .count() == 0:
                    db.session.add(FoodScore(food_temp, 'Nation', nation_temp.id, 1))
                else:
                    pass

            for i in request.json['tasteScore']:
                taste_temp = Taste.query.filter_by(tasteName=i['tasteName']).first()
                if FoodScore.query.filter(FoodScore.food_id == food_temp.id)\
                                  .filter(FoodScore.targetEnum == 'Taste')\
                                  .filter(FoodScore.targetId == taste_temp.id)\
                                  .count() == 0:
                    db.session.add(FoodScore(food_temp, 'Taste', taste_temp.id, i['score']))
                else:
                    pass

            db.session.commit()
        return render_template("administrator/sb-admin/pages/food-score.html")

    @route('/foodscore/index/', methods=['POST', 'GET'])
    def foodscore_index(self):
        # score를 수정할경우
        if request.method == 'POST':
            food_id = Food.query.filter_by(foodName = request.json['foodName']).one().id
            temp = FoodScore.query.filter(FoodScore.food_id == food_id)\
                                  .filter(FoodScore.targetEnum == request.json['targetEnum'])\
                                  .filter(FoodScore.targetId == request.json['targetId'])\
                                  .one()
            temp.score = request.json['score']
            db.session.add(temp)
            db.session.commit()
            return 'good'

        return render_template("administrator/sb-admin/pages/food-score-table.html")

    @route('/foodscore/delete/', methods=['POST', 'GET'])
    def foodscore_delete(self):
        food_id = Food.query.filter_by(foodName=request.json['foodName'] ).one().id
        FoodScore.query.filter(FoodScore.food_id == food_id)\
                       .filter(FoodScore.targetEnum == request.json['targetEnum'])\
                       .filter(FoodScore.targetId == request.json['targetId']).delete()
        db.session.commit()
        return 'good'

    # FoodScore 데이터 받아오는 부분
    @route('/foodscore/getdata/', methods=['GET'])
    def get_foodscore(self):
        foodscore_cook_table = db.session.query(FoodScore, Cook)\
                                         .outerjoin(Cook, FoodScore.targetId == Cook.id)\
                                         .filter(FoodScore.targetEnum == 'Cook')
        foodscore_taste_table = db.session.query(FoodScore, Taste)\
                                          .outerjoin(Taste, FoodScore.targetId == Taste.id)\
                                          .filter(FoodScore.targetEnum == 'Taste')
        foodscore_nation_table = db.session.query(FoodScore, Nation)\
                                           .outerjoin(Nation, FoodScore.targetId == Nation.id)\
                                           .filter(FoodScore.targetEnum == 'Nation')

        return jsonify(
            {
                'foodscore_cook':
                    [
                        {
                            'food_id': item[0].food_id,
                            'id': item[0].id,
                            'foodName': item[0].food.foodName,
                            'targetName': item[1].cookName,
                            'targetId': item[0].targetId,
                            'targetEnum': item[0].targetEnum,
                            'score': item[0].score
                        } for item in foodscore_cook_table
                    ],
                'foodscore_taste':
                    [
                        {
                            'food_id': item[0].food_id,
                            'id': item[0].id,
                            'foodName': item[0].food.foodName,
                            'targetName': item[1].tasteName,
                            'targetId': item[0].targetId,
                            'targetEnum' : item[0].targetEnum,
                            'score' : item[0].score
                        } for item in foodscore_taste_table
                    ],
                'foodscore_nation':
                    [
                        {
                            'food_id': item[0].food_id,
                            'id': item[0].id,
                            'foodName' : item[0].food.foodName,
                            'targetName': item[1].nationName,
                            'targetId': item[0].targetId,
                            'targetEnum' : item[0].targetEnum,
                            'score' : item[0].score
                        } for item in foodscore_nation_table
                    ]
            }
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

            # food table에서 지우면 foodscore table에서도 지워지게
            get_food = Food.query.filter(Food.foodName == request.json['foodName']).first()
            foodscore_temp = FoodScore.query.filter(FoodScore.food_id == get_food.id)
            if foodscore_temp.count() > 0:
                foodscore_temp.delete()

            Food.query.filter_by(foodName=request.json['foodName']).delete()
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

            # cook table에서 지우면 foodscore table에서도 지워지게
            get_cook = Cook.query.filter(Cook.cookName == request.json['cookName']).first()
            foodscore_temp = FoodScore.query.filter(FoodScore.targetEnum == 'Cook')\
                                            .filter(FoodScore.targetId == get_cook.id)
            if foodscore_temp.count() > 0:
                foodscore_temp.delete()

            Cook.query.filter_by(cookName=request.json['cookName']).delete()
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

            # nation table에서 지우면 foodscore table에서도 지워지게
            get_nation = Nation.query.filter(Nation.nationName == request.json['nationName']).first()
            foodscore_temp = FoodScore.query.filter(FoodScore.targetEnum == 'Nation')\
                                            .filter(FoodScore.targetId == get_nation.id)
            if foodscore_temp.count() > 0:
                foodscore_temp.delete()

            Nation.query.filter_by(nationName=request.json['nationName']).delete()
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

            # taste table에서 지우면 foodscore table에서도 지워지게
            get_taste = Taste.query.filter(Taste.tasteName == request.json['tasteName']).first()
            foodscore_temp = FoodScore.query.filter(FoodScore.targetEnum == 'Taste')\
                                            .filter(FoodScore.targetId == get_taste.id)
            if foodscore_temp.count() > 0:
                foodscore_temp.delete()

            Taste.query.filter_by(tasteName=request.json['tasteName']).delete()
            db.session.commit()
        return 'seccess'

    @route('/user/', methods=['GET'])
    def user_index(self):
        return render_template("administrator/sb-admin/pages/user.html")

    @route('/time/', methods=['GET'])
    def time_index(self):
        return render_template("administrator/sb-admin/pages/time.html")

    @route('/time/add/', methods=['POST'])
    def addtime(self):
        if request.method == 'POST':
            print request.get_data()
            temp = Time(request.json['timeName'], request.json['startTime'])
            db.session.add(temp)
            db.session.commit()
        return 'seccess'

    @route('/time/delete/', methods=['POST'])
    def deletetime(self):
        if request.method == 'POST':
            print request.get_data()
            Time.query.filter_by(timeName=request.json['timeName']).delete()
            db.session.commit()
        return 'seccess'