# -*- coding: utf-8 -*-
__author__ = 'bagmyeongho'

#추가해야할 사항들
#샐러리를 이용하여 3일마다 한번씩 유저 짠맛,단맛,매운맛을 갱신하므로 3일마다 한번씩 User_score를 지워야됨
#알고리즘 ㅅㅂ



import random
from app.models import FoodScore, UserFoodScore, UserScore, User
from app import db


def evaluate_user_score(user):
    #변수선언
    max_rating = 5
    max_star = 5

    sum_salty = []
    sum_sweety = []
    sum_spicy = []
    sum_sour = []
    sum_bitter = [] # 쓴맛
    sum_roast_aromatic = [] # 고소한 맛
    sum_cool = [] #시원한 맛
    sum_greasy = [] #느끼한 맛
    sum_fresh = [] #개운한맛
    sum_crunky = [] #바삭한 맛
    sum_ruber = [] #졸깃한 맛

    sum_boil = [] #끓이기
    sum_hard_boil = [] #졸이기
    sum_steam = [] #찌기
    sum_fire= [] #볶기
    sum_fried = [] #튀기기
    sum_baked = [] #굽기
    sum_water = [] #삶기
    sum_spoiled = [] #삭히기
    sum_little_watter = [] #데치기

    #쿼리 선언
    # temp에 접속해 있는 유저가 평가한 음식의 점수를 모두 불러온다 user_id에는 나중에 현재 접속한 유저의 값이 들어오도록 수정
    user_food_score_by_id = UserFoodScore.query.filter_by(user_id = user.id).all()

    # 푸드스코어 쿼리
    food_score_by_taste = FoodScore.query.filter_by(targetEnum = 'Taste').all()
    food_score_by_cook = FoodScore.query.filter_by(targetEnum = 'Cook').all()

    # 유저의 개인이 평가한 맛의 평균을 구하는 식
    # 짠맛
    for v in user_food_score_by_id:
        usersalt_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 1).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_salty.append(usersalt_temp)

    user_salty = (sum(sum_salty) / (max_rating * max_star * float(len(sum_salty))))*4+1
    object_temp = UserScore(user.id, "Taste", 1, round(user_salty, 2))  # 짠맛 targetId = 1
    db.session.add(object_temp)

    # print round(user_salty, 2)

    # 단맛
    for v in user_food_score_by_id:
        usersweety_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                              .filter_by(targetId = 2).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        sum_sweety.append(usersweety_temp)

    user_sweety = (sum(sum_sweety) / (max_rating * max_star * float(len(sum_sweety))))*4+1

    # print round(user_sweety, 2)
    object_temp = UserScore(user.id, "Taste", 2, round(user_sweety, 2)) # 단맛 targetId = 2
    db.session.add(object_temp)

    #매운맛
    for v in user_food_score_by_id:
        userspicy_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                             .filter_by(targetId = 3).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        sum_spicy.append(userspicy_temp)

    user_spicy = (sum(sum_spicy) / (max_rating * max_star * float(len(sum_spicy))))*4+1

    # print round(user_spicy, 2)
    object_temp = UserScore(user.id, "Taste", 3, round(user_spicy, 2)) # 매운맛 targetId = 3
    db.session.add(object_temp)

    # 신맛
    for v in user_food_score_by_id:
        usersour_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 4).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_sour.append(usersour_temp)

    user_sour = (sum(sum_sour) / (max_star * float(len(sum_sour))))
    object_temp = UserScore(user.id, "Taste", 4, round(user_sour, 2))  # 신맛 targetId = 4
    db.session.add(object_temp)

    # 쓴맛
    for v in user_food_score_by_id:
        userbitter_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 5).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_bitter.append(userbitter_temp)

    user_bitter = (sum(sum_bitter) / (max_star * float(len(sum_bitter))))
    object_temp = UserScore(user.id, "Taste", 5, round(user_bitter, 2))  # 쓴 맛 targetId = 5
    db.session.add(object_temp)

    # 고소한 맛
    for v in user_food_score_by_id:
        user_roast_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 6).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_roast_aromatic.append(user_roast_temp)

    user_roast = (sum(sum_roast_aromatic) / (max_star * float(len(sum_roast_aromatic))))
    object_temp = UserScore(user.id, "Taste", 6, round(user_roast, 2))  # 고소한 맛 targetId = 6
    db.session.add(object_temp)

    # 시원한 맛
    for v in user_food_score_by_id:
        usercool_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 7).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_cool.append(usercool_temp)

    user_cool = (sum(sum_cool) / (max_star * float(len(sum_cool))))
    object_temp = UserScore(user.id, "Taste", 7, round(user_cool, 2))  # 시원한 맛 targetId = 7
    db.session.add(object_temp)

    # 느끼한 맛
    for v in user_food_score_by_id:
        user_greasy_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 8).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_greasy.append(user_greasy_temp)

    user_greasy = (sum(sum_greasy) / (max_star * float(len(sum_greasy))))
    object_temp = UserScore(user.id, "Taste", 8, round(user_greasy, 2))  # 느끼한 맛 targetId = 8
    db.session.add(object_temp)

    # 개운한 맛
    for v in user_food_score_by_id:
        userfresh_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 9).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_fresh.append(userfresh_temp)

    user_fresh = (sum(sum_fresh) / (max_star * float(len(sum_fresh))))
    object_temp = UserScore(user.id, "Taste", 9, round(user_fresh, 2))  # 개운한 맛 targetId = 9
    db.session.add(object_temp)

    # 바삭한 맛
    for v in user_food_score_by_id:
        usercrunky_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 10).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_crunky.append(usercrunky_temp)

    user_crunky = (sum(sum_crunky) / (max_star * float(len(sum_crunky))))
    object_temp = UserScore(user.id, "Taste", 10, round(user_crunky, 2))  # 바삭한 맛 targetId = 10
    db.session.add(object_temp)

    # 쫄깃한 맛
    for v in user_food_score_by_id:
        user_rubber_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Taste")\
                            .filter_by(targetId = 11).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴

        sum_ruber.append(user_rubber_temp)

    user_rubber = (sum(sum_ruber) / (max_star * float(len(sum_ruber))))
    object_temp = UserScore(user.id, "Taste", 11, round(user_rubber, 2))  # 쫄깃한 맛 targetId = 11
    db.session.add(object_temp)

    #조리법에 대한 필터링
    # 끓이기
    for v in user_food_score_by_id:
        try:
            userboil_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 1).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            userboil_temp = 0

        sum_boil.append(userboil_temp)

    user_boil = (sum(sum_boil) / (max_star * float(len(sum_boil))))
    object_temp = UserScore(user.id, "Cook", 1, round(user_boil, 2))  # 끓이기 targetId = 1
    db.session.add(object_temp)

    # 졸이기
    for v in user_food_score_by_id:
        try:
            user_hard_boil_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 2).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            user_hard_boil_temp = 0

        sum_hard_boil.append(user_hard_boil_temp)

    user_hard_boil = (sum(sum_hard_boil) / (max_star * float(len(sum_hard_boil))))
    object_temp = UserScore(user.id, "Cook", 2, round(user_hard_boil, 2))  # 졸이기 targetId = 2
    db.session.add(object_temp)

    # 찌기
    for v in user_food_score_by_id:
        try:
            usersteam_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 3).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            usersteam_temp = 0

        sum_steam.append(usersteam_temp)

    user_steam = (sum(sum_steam) / (max_star * float(len(sum_steam))))
    object_temp = UserScore(user.id, "Cook", 3, round(user_steam, 2))  # 찌기 targetId = 3
    db.session.add(object_temp)

    # 볶기
    for v in user_food_score_by_id:
        try:
            userfire_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 4).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            userfire_temp = 0

        sum_fire.append(userfire_temp)

    user_fire = (sum(sum_fire) / (max_star * float(len(sum_fire))))
    object_temp = UserScore(user.id, "Cook", 4, round(user_fire, 2))  # 볶기 targetId = 4
    db.session.add(object_temp)

    # 튀기기
    for v in user_food_score_by_id:
        try:
            userfried_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 5).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            userfried_temp = 0

        sum_fried.append(userfried_temp)

    user_fried = (sum(sum_fried) / (max_star * float(len(sum_fried))))
    object_temp = UserScore(user.id, "Cook", 5, round(user_fried, 2))  # 튀기기 targetId = 5
    db.session.add(object_temp)

    # 굽기
    for v in user_food_score_by_id:
        try:
            userbake_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 6).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            userbake_temp = 0

        sum_baked.append(userbake_temp)

    user_bake = (sum(sum_baked) / (max_star * float(len(sum_baked))))
    object_temp = UserScore(user.id, "Cook", 6, round(user_bake, 2))  # 굽기 targetId = 6
    db.session.add(object_temp)

    # 삶기
    for v in user_food_score_by_id:
        try:
            userwater_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 7).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            userwater_temp = 0

        sum_water.append(userwater_temp)

    user_water = (sum(sum_water) / (max_star * float(len(sum_water))))
    object_temp = UserScore(user.id, "Cook", 7, round(user_water, 2))  # 삶기 targetId = 7
    db.session.add(object_temp)

    # 삭히기
    for v in user_food_score_by_id:
        try:
            userspoil_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 8).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            userspoil_temp = 0

        sum_spoiled.append(userspoil_temp)

    user_spoiled = (sum(sum_spoiled) / (max_star * float(len(sum_spoiled))))
    object_temp = UserScore(user.id, "Cook", 8, round(user_spoiled, 2))  # 삭히기 targetId = 8
    db.session.add(object_temp)

    # 데치기
    for v in user_food_score_by_id:
        try:
            user_little_water_temp = FoodScore.query.filter_by(food_id = v.food_id).filter_by(targetEnum = "Cook")\
                                .filter_by(targetId = 9).one().score * v.score # temp가 UserFoodScore의 쿼리를 이미 받아옴
        except:
            user_little_water_temp = 0

        sum_little_watter.append(user_little_water_temp)

    user_little_water = (sum(sum_little_watter) / (max_star * float(len(sum_little_watter))))
    object_temp = UserScore(user.id, "Cook", 9, round(user_little_water, 2))  # 데치기 targetId = 9
    db.session.add(object_temp)

    # score_list엔 각각의 음식의 맛 점수와 유저가 가지고있는 맛의 점수를 비교하여 차이가 가장 적은 것을 선택해주는 알고리즘을 이용중이다.

    temp_dic = {}

    # 유사도 공식 = abs(temp['짠맛']-user_salty) + abs(temp['단맛']-user_sweety) + abs(temp['매운맛']-user_spicy)
    # 아래 식은 딕셔너리의 키값을 검사하여 키값이 있으면 유사도를 더하고, 없으면 키값을 추가하여 유사도를 더하는 알고리즘
    for v in food_score_by_taste:
        temp_name = v.food.foodName
        sim = 0
        if temp_name in temp_dic:
            if v.targetId == 1:
                sim = abs(v.score - user_salty)
            elif v.targetId == 2:
                sim = abs(v.score - user_sweety)
            elif v.targetId == 3:
                sim = abs(v.score - user_spicy)
            elif v.targetId == 4:
                sim = abs(v.score - user_sour)
            elif v.targetId == 5:
                sim = abs(v.score - user_bitter)
            elif v.targetId == 6:
                sim = abs(v.score - user_roast)
            elif v.targetId == 7:
                sim = abs(v.score - user_cool)
            elif v.targetId == 8:
                sim = abs(v.score - user_greasy)
            elif v.targetId == 9:
                sim = abs(v.score - user_fresh)
            elif v.targetId == 10:
                sim = abs(v.score - user_crunky)
            elif v.targetId == 11:
                sim = abs(v.score - user_rubber)
            temp_dic[temp_name] += round(sim, 2)
        else :
            if v.targetId == 1:
                sim = abs(v.score - user_salty)
            elif v.targetId == 2:
                sim = abs(v.score - user_sweety)
            elif v.targetId == 3:
                sim = abs(v.score - user_spicy)
            elif v.targetId == 4:
                sim = abs(v.score - user_sour)
            elif v.targetId == 5:
                sim = abs(v.score - user_bitter)
            elif v.targetId == 6:
                sim = abs(v.score - user_roast)
            elif v.targetId == 7:
                sim = abs(v.score - user_cool)
            elif v.targetId == 8:
                sim = abs(v.score - user_greasy)
            elif v.targetId == 9:
                sim = abs(v.score - user_fresh)
            elif v.targetId == 10:
                sim = abs(v.score - user_crunky)
            elif v.targetId == 11:
                sim = abs(v.score - user_rubber)
            temp_dic[temp_name] = round(sim, 2)

    #final_list엔 최종적으로 맛의 유사도가 높은 것들 10개를 선정하여 저장한다.
    random_list= []

    #temp_dic에 있는 모든 음식과 그 음식의 유사도에서 value값이 최소인 것들을 차례대로 pop하여 final_list에 넣는다.
    for v in range(0, 10):
        random_list.append(min(temp_dic, key=temp_dic.get))
        temp_dic.pop(min(temp_dic, key=temp_dic.get), None)

    db.session.commit()
    #일단 DB에 넣는 과정은 생략함
    return random_list[random.randrange(0,10)]
