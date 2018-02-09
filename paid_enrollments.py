# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 15:40:58 2018

@author: Ajay
"""

from fixing_data_types import fixing_data_types
def paid_enrollments(file):
    enrollments = fixing_data_types(file)
    paid_enrollments = []
    for enrollment in enrollments:
        if (enrollment['days_to_cancel'] == None or enrollment['days_to_cancel'] > 7) and not enrollment['is_udacity']:
            paid_enrollments.append(enrollment['account_key'])
    return(set(paid_enrollments))