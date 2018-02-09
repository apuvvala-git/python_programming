# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:25:26 2018

@author: Ajay
"""

def hours2days(hours):
    ndays = hours // 24
    nhours = hours % 24 
    t = (ndays, nhours)
    return (t)