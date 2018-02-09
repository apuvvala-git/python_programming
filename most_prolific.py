# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 22:13:05 2018

@author: Ajay

most_prolific: Find the most prolific year for given discography

Example:
    Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
    "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
    "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
    "Sgt. Pepper's Lonely Hearts Club Band": 1967,
    "Magical Mystery Tour": 1967, "The Beatles": 1968,
    "Yellow Submarine": 1969 ,'Abbey Road': 1969,
    "Let It Be": 1970}
    
    most_prolific(Beatles_Discography)
    
    returns 1964
"""

def most_prolific(discography):
    years = {}
    for album_title in discography:
        if discography[album_title] in years:
            years[discography[album_title]] += 1
        else:
            years[discography[album_title]] = 1

    return(max(years, key=years.get))

