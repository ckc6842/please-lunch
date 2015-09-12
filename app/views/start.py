# -*- coding: utf-8 -*-
from flask import render_template, redirect, url_for, flash, jsonify, request
from flask_classy import FlaskView, route
from flask_security import login_required, current_user
from app.models import Food, User, UserFoodScore
from app import db


class StartView(FlaskView):
    decorators = [login_required]
    route_base = '/start/'

    def index(self):
        if current_user.is_evaluate:
            return redirect(url_for('MainView:recommend'))
        else:
            return render_template('start/index.html')

    def post(self):
        print 'post'
        if not current_user.is_evaluate:
            if request.method == 'POST':
                food_id = Food.query.filter_by(foodName=request.json['foodName']).one().id
                temp = UserFoodScore.query.filter_by(user_id=request.json['userId']).filter_by(food_id=food_id)

                if temp.count() > 0:        # 이미 평가한 음식이라면 스코어만 업데이트
                    temp.score = int(request.json['rating'])
                    db.session.commit()
                else:
                    temp = UserFoodScore(int(request.json['userId']), food_id, request.json['rating'])
                    db.session.add(temp)
                    db.session.commit()

            if UserFoodScore.query.filter_by(user_id=request.json['userId']).count() > 2:       # 평가한 음식 갯수가 10개가 됐나?
                current_user.is_evaluate = True
                db.session.commit()
                return redirect(url_for('StartView:evaluate'))

            print 'good'
            current_user.is_evaluate = True
            flash('Your information successfully evaluated!')
            return redirect(url_for('StartView:evaluate'))
        else:
            flash('You are already evaluated')
            return redirect(url_for('MainView:recommend'))

    def evaluate(self):
        return redirect(url_for('MainView:recommend'))

    @route('/getfoodlist/', methods=['GET', 'POST'])
    def getfoodlist(self):
        foodqueried =  Food.query.all()

        foodlist = {'foodlist': [{'id': food.id, 'foodName': food.foodName, 'image': food.img} for food in foodqueried]}

        return jsonify(foodlist)
