# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 21:00:22 2018

@author: Ajay
"""

def readable_timedelta(days):
    """ readable_timedelta - Returns readable timedelta
    
        days - # of days. Type: int
    """
    nweeks = days // 7
    nmoddays = days % 7
    
    str = "{0} week(s) and {1} day(s)".format(nweeks, nmoddays)
    return str

# Uncomment this function call to test it:
print(readable_timedelta(10))

