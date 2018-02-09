# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:46:10 2018

@author: Ajay
"""

def delete_free_trial_cancels(data, paid_students):
    new_data = []
    for point in data:
        if point['account_key'] in paid_students:
            new_data.append(point)
    return new_data