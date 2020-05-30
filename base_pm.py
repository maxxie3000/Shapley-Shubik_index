#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:17:46 2020

List for parties:
    0: number_of_seats
    1: number of final votes
    2: relative of final votes to total permutations
    3: ratio power to number of seats 
    4: number of seats in power 
    5: round round 2
    

@author: Max
"""
import user_interaction

from itertools import permutations

def shsu():
    print("Let's see how the power is divide according to the Shapley-Shubik index\n First, let's get the basics:")
    number_of_seats, majority_vote, parties = user_interaction.get_inputs()
   #Number of seats for majority vote
    seats_mv = number_of_seats * (majority_vote/100)
   #Number of permutation user itertools
    perm = permutations(parties)   
    total_iterations = 0
    for p in parties:
        parties[p].append(0)
    winner_list = [1]
    loc = 0
   #Loop through perm 
    for pe in perm:
        #itertools does not provide len function
        total_iterations += 1
        print("\n iteration number: {0} \n check {1}".format(total_iterations, pe))
        if pe[:(loc+1)] == winner_list:
            decider = winner_list[-1]
            parties[decider][1] += 1
            print("win by known pattern {0}".format(p))
        else:    
          total_votes = 0
      #loop through specific permutation
          for p in pe:
          #increase total votes of the group of parties 
            total_votes += parties[p][0]
            if total_votes >= seats_mv:
               
               parties[p][1] += 1
               loc = pe.index(p)
               winner_list = pe[:loc+1]
               print("win by {0}".format(p))
               break       
  
    for p in parties:
         #Making relative deceiding vote 
        parties[p].append(parties[p][1]/total_iterations)
       #Creating ratio between power and number of seats 
        ratio = (parties[p][2]) / (parties[p][0]/number_of_seats)
        rratio = round(ratio, 2)
        parties[p].append(rratio)
       #The number of seats according to power calculation 
        parties[p].append(round(ratio*number_of_seats))
        parties[p].append(round(parties[p][2],2))
    
    user_interaction.output(parties)
    return