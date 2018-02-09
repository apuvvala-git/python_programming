# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 20:45:01 2018

@author: Ajay
"""

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days < 7

