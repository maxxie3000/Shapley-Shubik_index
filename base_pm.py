#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:17:46 2020

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
   #Creating dictionary to count decisive votes of parties  
    parties_dec = {}
    for p in parties:
        parties_dec[p] = 0   
    total_iterations = 0
   #Loop through perm 
    for pe in perm:
       total_votes = 0
      #itertools does not provide len function
       total_iterations += 1
      #loop through specific permutation
       for p in pe:
          #increase total votes of the group of parties 
           total_votes += parties[p]
           if total_votes > seats_mv:
               parties_dec[p] += 1
               break       
   #This needs to go to user_interactions 
    for p in parties_dec:
        print("\n{0} has {1} power index versus {2} relative seat number".format(p, parties_dec[p]/total_iterations, parties[p]/number_of_seats))
    return
