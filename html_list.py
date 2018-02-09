# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 21:23:59 2018

@author: Ajay
"""

#define the  html_list function
def html_list(string_list):
    out_string = ["<ul>"]
    for item in string_list:
        out_string.append("<li>{0}</li>".format(item))
    out_string.append("</ul>")
    out_string = "\n".join(out_string)
    print(out_string)