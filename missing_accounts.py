# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 22:05:50 2018

@author: Ajay
"""

def missing_accounts(enrollments, engagements):
    
    d = enrollments.symmetric_difference(engagements)
    
    for item in d:
        print(item)
