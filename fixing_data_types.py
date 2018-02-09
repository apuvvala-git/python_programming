# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 10:40:55 2018

@author: Ajay
"""

def fixing_data_types(filename):
    from datetime import datetime as dt
    import unicodecsv

    ## Longer version of code (replaced with shorter, equivalent version below)

    # enrollments = []
    # f = open('enrollments.csv', 'rb')
    # reader = unicodecsv.DictReader(f)
    # for row in reader:
    #     enrollments.append(row)
    # f.close()
    
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        enrollments = list(reader)
         
        # Takes a date as a string, and returns a Python datetime object. 
        # If there is no date given, returns None
        def parse_date(date):
            if date == '':
                return None
            else: 
                return dt.strptime(date, '%Y-%m-%d')
    
    # Takes a string which is either an empty string or represents an integer,
    # and returns an int or None.
    def parse_maybe_int(i):
        if i == '':
            return None
        else:
            return int(i)

    # Clean up the data types in the enrollments table
    for enrollment in enrollments:
        enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
        enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
        enrollment['is_canceled'] = enrollment['is_canceled'] == 'True'
        enrollment['is_udacity'] = enrollment['is_udacity'] == 'True'
        enrollment['join_date'] = parse_date(enrollment['join_date'])
    
    return(enrollments)

