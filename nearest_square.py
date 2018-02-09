# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 21:20:46 2018

@author: Ajay
"""

#TODO: Implement the nearest_square function
def nearest_square(limit):
    
    num = 0
    sq_number = 0
    
    while (sq_number < limit):
        num += 1
        new_sq_number = num**2
        if new_sq_number < limit:
            sq_number = new_sq_number
        else:
            break
    return(sq_number)