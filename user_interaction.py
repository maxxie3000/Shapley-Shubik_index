#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:17:44 2020

@author: Max
"""

def get_inputs():
    number_of_seats = int(input("What is the number of seats? "))
    majority_vote = int(input("What is the relative cut-off for majority vote? "))
    filled_seats = 0
    parties = {}
    while filled_seats < number_of_seats: 
        party = input("Party name: ")
        seats = int(input("How many seat does {0} have? ".format(party)))
        parties[party] = seats
        filled_seats += seats
    if not filled_seats == number_of_seats:
        print("The number of seats and filled seats are not the same, try again\n")
        get_inputs()
    for n in parties:
        print("\n{0} has {1} number of seats".format(n, parties[n]))
    return number_of_seats, majority_vote, parties
    
