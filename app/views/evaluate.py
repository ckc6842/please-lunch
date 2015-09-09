# -*- coding: utf-8 -*-
__author__ = 'bagmyeongho'

from collections import defaultdict
from operator import itemgetter


# Dummy Data
zajangmyun = {"짠맛" : 1, "단맛" : 2, "매운맛" : 1, "name" : "zajangmyun"}
ramyun = {"짠맛" : 1, "단맛" : 1, "매운맛" : 3, "name" : "ramyun"}
dduk = {"짠맛" : 1, "단맛" : 1, "매운맛" : 1, "name" : "dduk"}

user_zajangmyun= {"star" : 1}
user_ramyun = {"star" : 5}
user_dduk = {"star" : 1}

food_list = [zajangmyun, ramyun, dduk]

max_rating = 5
max_star = 5
max_score = float(max_rating * max_star * 3)


#유저가 평가한 모든 음식의 맛 평균값을 저장하게된다. 현재는 단맛, 짠맛, 매운맛 밖에 없으니 3개의 변수가 있다.
user_salty = (((zajangmyun['짠맛'] * user_zajangmyun['star']) +
               (ramyun['짠맛']* user_ramyun['star']) +
               (dduk['짠맛']* user_dduk['star'])) / max_score)*4+1

user_sweety = (((zajangmyun['단맛'] * user_zajangmyun['star']) +
               (ramyun['단맛']* user_ramyun['star']) +
               (dduk['단맛']* user_dduk['star'])) / max_score)*4+1

user_spicy = (((zajangmyun['매운맛'] * user_zajangmyun['star']) +
               (ramyun['매운맛']* user_ramyun['star']) +
               (dduk['매운맛']* user_dduk['star'])) / max_score)*4+1

user_taste = [user_salty, user_sweety, user_spicy]


score_list = {}

# 딕셔너리 val값을 비교하여 최소인 key값을 출력해주는 함수
def get_res(dVals):
    res = defaultdict(list)
    for k, v in dVals.items():
        res[v].append(k)
    return min(res.items(), key=itemgetter(0))[1]


# score_list엔 각각의 음식의 맛 점수와 유저가 가지고있는 맛의 점수를 비교하여 차이가 가장 적은 것을 선택해주는 알고리즘을 이용중이다.
for temp in food_list :
   score_list[temp["name"]] = abs(temp['짠맛']-user_salty) + abs(temp['단맛']-user_sweety) + abs(temp['매운맛']-user_spicy)

print score_list.values() # 현재 score_list에 있는 음식은 총 3개로 자장면, 떡, 라면 순으로 리스트에 넣어지는 것 같다.

print get_res(score_list) # get_res라는 함수를 이용하여 score_list에 들어있는 가장 최소값의 value값을 가진  Key값을 출력한다.

