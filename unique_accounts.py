# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:51:52 2018

@author: Ajay
"""

def unique_accounts(enrollments):
    accounts = []
    for item in enrollments:
        accounts.append(item['acct'])
    return set(accounts)

