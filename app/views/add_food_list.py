# -*- coding: utf-8 -*-
__author__ = 'bagmyeongho'

import random
from app.models import FoodScore, UserScore, UserFood, Time
from app import db

def add_food_list(user):

    final_cook_list = []
    final_nation_list = []
    final_random_list = []

    time_query = Time.query.first()
    user_nation_score = UserScore.query.filter_by(targetEnum = 'Nation').filter_by(user_id = user.id).all()
    user_cook_score = UserScore.query.filter_by(targetEnum = 'Cook').filter_by(user_id = user.id).all()
    food_score_by_taste = FoodScore.query.filter_by(targetEnum = 'Taste').all()

    user_salty = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 1)\
        .first()
    user_sweety = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 2)\
        .first()
    user_spicy = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 3)\
        .first()
    user_sour = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 4)\
        .first()
    user_bitter = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 5)\
        .first()
    user_roast = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 6)\
        .first()
    user_cool = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 7)\
        .first()
    user_greasy = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 8)\
        .first()
    user_fresh = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 9)\
        .first()
    user_crunky = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 10)\
        .first()
    user_rubber = UserScore.query.filter_by(targetEnum = 'Taste').filter_by(user_id = user.id).filter_by(targetId = 11)\
        .first()


    temp_dic = {}
    # 유저가 어떤 국가의 음식을 가장 선호하는지 구하기
    temp_nation = user_nation_score[0]
    for v in user_nation_score:
        if v.score > temp_nation.score:
            temp_nation = v

    best_user_nation = temp_nation.targetId

    # 유저가 어떤 조리법의 음식을 가장 선호하는지 구하기
    temp_cook = user_cook_score[0]
    for v in user_cook_score:
        if v.score > temp_cook.score:
            temp_cook = v

    best_user_cook = temp_cook.targetId

    filter_cook_list = FoodScore.query.filter_by(targetEnum = 'Cook').filter_by(targetId = best_user_cook).all()
    filter_nation_list = FoodScore.query.filter_by(targetEnum = 'Nation').filter_by(targetId = best_user_nation).all()

    random.shuffle(filter_cook_list)
    random.shuffle(filter_nation_list)
    random.shuffle(food_score_by_taste)

    for k in filter_cook_list:
        final_cook_list.append(k)
        filter_cook_list.pop(0)
        if len(final_cook_list) == 5:
            break

    for k in filter_nation_list:
        final_nation_list.append(k)
        filter_nation_list.pop(0)
        if len(final_nation_list) == 5:
            break

    for k in food_score_by_taste:
        final_random_list.append(k)
        food_score_by_taste.pop(0)
        if len(final_random_list) == 10:
            break


    final_list = final_random_list + final_cook_list + final_nation_list

    #중복검사
    temp_food_id = []
    for k in final_list:
        temp_food_id.append(k.food_id)

    temp_food_id = set(temp_food_id)
    temp_food_id = list(temp_food_id)

    taste_list = []
    for k in temp_food_id:
        taste_list.append(FoodScore.query.filter_by(targetEnum = 'Taste').filter_by(food_id = k).all())

    # for k in taste_list:
    #     for v in k:
    #         print v.food.foodName

    # score_list엔 각각의 음식의 맛 점수와 유저가 가지고있는 맛의 점수를 비교하여 차이가 가장 적은 것을 선택해주는 알고리즘을 이용중이다.
    # 유사도 공식 = abs(temp['짠맛']-user_salty) + abs(temp['단맛']-user_sweety) + abs(temp['매운맛']-user_spicy)
    # 아래 식은 딕셔너리의 키값을 검사하여 키값이 있으면 유사도를 더하고, 없으면 키값을 추가하여 유사도를 더하는 알고리즘
    for v in taste_list:
        for k in v:
            temp_name = k.food_id
            sim = 0
            if temp_name in temp_dic:
                if k.targetId == 1:
                    sim = abs(k.score - user_salty.score)
                elif k.targetId == 2:
                    sim = abs(k.score - user_sweety.score)
                elif k.targetId == 3:
                    sim = abs(k.score - user_spicy.score)
                elif k.targetId == 4:
                    sim = abs(k.score - user_sour.score)
                elif k.targetId == 5:
                    sim = abs(k.score - user_bitter.score)
                elif k.targetId == 6:
                    sim = abs(k.score - user_roast.score)
                elif k.targetId == 7:
                    sim = abs(k.score - user_cool.score)
                elif k.targetId == 8:
                    sim = abs(k.score - user_greasy.score)
                elif k.targetId == 9:
                    sim = abs(k.score - user_fresh.score)
                elif k.targetId == 10:
                    sim = abs(k.score - user_crunky.score)
                elif k.targetId == 11:
                    sim = abs(k.score - user_rubber.score)
                temp_dic[temp_name] += round(sim, 2)
            else :
                if k.targetId == 1:
                    sim = abs(k.score - user_salty.score)
                elif v.targetId == 2:
                    sim = abs(k.score - user_sweety.score)
                elif v.targetId == 3:
                    sim = abs(k.score - user_spicy.score)
                elif v.targetId == 4:
                    sim = abs(k.score - user_sour.score)
                elif v.targetId == 5:
                    sim = abs(k.score - user_bitter.score)
                elif v.targetId == 6:
                    sim = abs(k.score - user_roast.score)
                elif v.targetId == 7:
                    sim = abs(k.score - user_cool.score)
                elif v.targetId == 8:
                    sim = abs(k.score - user_greasy.score)
                elif v.targetId == 9:
                    sim = abs(k.score - user_fresh.score)
                elif v.targetId == 10:
                    sim = abs(k.score - user_crunky.score)
                elif v.targetId == 11:
                    sim = abs(k.score - user_rubber.score)
                temp_dic[temp_name] = round(sim, 2)

    # for k,v in temp_dic.items():
    #     print k,v


    sorted_food = sorted(temp_dic.items(), key=lambda x: x[1])
    ten_food= []
    for k in dict(sorted_food).keys():
        ten_food.append(k)
        if len(ten_food) == 10:
            break


    for k in ten_food:
         final_final = UserFood(user.id, k, time_query.id)
         db.session.add(final_final)

    #temp_dic에 있는 모든 음식과 그 음식의 유사도에서 value값이 최소인 것들을 차례대로 pop하여 final_list에 넣는다.

    db.session.commit()
    #일단 DB에 넣는 과정은 생략함
    return ten_food[random.randrange(0,10)]