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

    @route('/getfoodlist/', methods=['GET', 'POST'])
    def getfoodlist(self):
        return jsonify({'foodlist' : [      # 어떤 음식을 평가하게할지?
            {'id' : 1, 'foodName' : '짜장면', 'image' : 'http://korcan50years.files.wordpress.com/2014/02/ed9884eb8c80-eca79cec9ea5eba9b4.jpg'},
            {'id' : 2, 'foodName' : '떡', 'image' : 'http://cfile239.uf.daum.net/image/1502AA3A4E5DD5EB151A4C'},
            {'id' : 3, 'foodName' : '라면', 'image' : 'http://dimg.tagstory.com/dailypod/article/488.jpg'},
        ]})
