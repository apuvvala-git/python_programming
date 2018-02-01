# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 11:55:35 2018

@author: Ajay
"""

def which_prize(points):
    prize = None
    if points <= 50:
        prize = "a wooden rabbit"
    elif 151 <= points <= 180:
        prize = "a wafer-thin mint"
    elif points >= 181:
        prize = "a penguin"

    if prize:
        return("Congratulations! You have won a {0}!".format(prize))
    else:
        return("Oh dear, no prize this time.")
