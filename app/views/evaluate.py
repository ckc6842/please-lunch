# -*- coding: utf-8 -*-
__author__ = 'bagmyeongho'

from collections import defaultdict
from operator import itemgetter
from app.models import FoodScore, UserFoodScore, UserScore
from app import db


def recommend_food(user):
    max_rating = 5
    max_star = 5
    max_score = float(max_rating * max_star * 3)

    sum_salty = []
    sum_sweety = []
    sum_spicy = []

    # temp에 접속해 있는 유저가 평가한 음식의 점수를 모두 불러온다 user_id에는 나중에 현재 접속한 유저의 값이 들어오도록 수정
    temp = UserFoodScore.query.filter_by(user_id = user.id).all()
    #푸드스코어 쿼리
    Food_temp = FoodScore.query.filter_by(targetEnum = 'Taste').all()

    score_list = {}

    # 딕셔너리 val값을 비교하여 최소인 key값을 출력해주는 함수
    def get_res(dVals):
        res = defaultdict(list)
        for k, v in dVals.items():
            print k,v
            res[v].append(k)
        return min(res.items(), key=itemgetter(0))[1]


    # 유저의 개인이 평가한 맛의 평균을 구하는 식
    #짠맛
    for v in temp :
        usersalt_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 1).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_salty.append(usersalt_temp)

    user_salty = (sum(sum_salty) / (max_rating * max_star * float(len(sum_salty))))*4+1
    object_temp = UserScore(2, "Taste", 1, round(user_salty, 2))  # 짠맛 targetId = 1
    db.session.add(object_temp)

    print round(user_salty, 2)

    # 단맛
    for v in temp :
        usersweety_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                              .filter_by(targetId = 2).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        sum_sweety.append(usersweety_temp)

    user_sweety = (sum(sum_sweety) / (max_rating * max_star * float(len(sum_sweety))))*4+1

    print round(user_sweety, 2)
    object_temp = UserScore(2, "Taste", 2, round(user_sweety, 2)) # 단맛 targetId = 2
    db.session.add(object_temp)

    #매운맛
    for v in temp :
        userspicy_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                             .filter_by(targetId = 3).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        sum_spicy.append(userspicy_temp)

    user_spicy = (sum(sum_spicy) / (max_rating * max_star * float(len(sum_spicy))))*4+1

    print round(user_spicy, 2)
    object_temp = UserScore(2, "Taste", 3, round(user_spicy, 2)) # 매운맛 targetId = 3
    db.session.add(object_temp)
    db.session.commit()
    # score_list엔 각각의 음식의 맛 점수와 유저가 가지고있는 맛의 점수를 비교하여 차이가 가장 적은 것을 선택해주는 알고리즘을 이용중이다.

    temp_dic = {}

    # 유사도 공식 = abs(temp['짠맛']-user_salty) + abs(temp['단맛']-user_sweety) + abs(temp['매운맛']-user_spicy)
    # 아래 식은 딕셔너리의 키값을 검사하여 키값이 있으면 유사도를 더하고, 없으면 키값을 추가하여 유사도를 더하는 알고리즘
    for v in Food_temp:
        temp_name = v.food.foodName
        sim = 0
        if temp_name in temp_dic:
            if v.targetId == 1:
                sim = abs(v.score - user_salty)
            elif v.targetId == 2:
                sim = abs(v.score - user_salty)
                sim = abs(v.score - user_sweety)
            elif v.targetId == 3:
                sim = abs(v.score - user_spicy)
            temp_dic[temp_name] += round(sim, 2)
        else :
            if v.targetId == 1:
                sim = abs(v.score - user_salty)
            elif v.targetId == 2:
                sim = abs(v.score - user_sweety)
            elif v.targetId == 3:
                sim = abs(v.score - user_spicy)
            temp_dic[temp_name] = round(sim, 2)

    # print get_res(score_list) # get_res라는 함수를 이용하여 score_list에 들어있는 가장 최소값의 value값을 가진  Key값을 출력한다.
    return get_res(temp_dic)[0].decode('utf-8')




    #
    # print min(score_list, key= score_list.get)


