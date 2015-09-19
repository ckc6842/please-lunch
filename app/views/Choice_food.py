# -*- coding: utf-8 -*-
__author__ = 'bagmyeongho'

import random
from app.models import UserFood

def choice_food(user):
    food_list = UserFood.query.filter_by(user_id = user.id).all()
    food_name_list = []
    for k in food_list:
        food_name_list.append(k.food.foodName)


    return random.choice(food_name_list)