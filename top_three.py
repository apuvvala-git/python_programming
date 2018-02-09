# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 19:43:03 2018

@author: Ajay
"""

def top_three(input_list):
    """Returns a list of the three largest elements input_list in order from largest to smallest.

    If input_list has fewer than three elements, return input_list element sorted largest to smallest/
    """
    # TODO: implement this function
    
    s_list = sorted(input_list, reverse=True)
    return s_list[0:3]

