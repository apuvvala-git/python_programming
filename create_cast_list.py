# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 22:10:57 2018

@author: Ajay
"""

def create_cast_list(filename):
    cast_list = []
    #use with to open the file filename
    #use the for loop syntax to process each line
    #and add the actor name to cast_list

    with open (filename, 'r') as f:
        for line in f:
            sline = line.split(',')
            cast_list.append(sline[0])
    return cast_list