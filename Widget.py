#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 22:04:20 2020

@author: jntrcs
"""

from itertools import combinations_with_replacement, combinations


class Widget:
    def __init__(self):
        self.start_state = 0
        self.end_states = []
        
    def __init__(self, start_id, end_ids, outer_graph):
        self.start_id = start_id
        self.end_ids = end_ids
        self.outer_graph = outer_graph
        self.inner_widget = self.generate_inner_widget()
        self.expected_values = self.generate_expected_values()
        
    def generate_inner_widget(self):
        combos = list(combinations_with_replacement([1, 2, 3, 4, 5, 6], 5))
        
        state_1 = {} #Rolls to options
        
        for i in combos:
            state_1[i] = []
            for x in range(5):
                possible_keeps = list(set(list(combinations(i, x+1))))
                state_1[i].extend(possible_keeps)
        
        
        state_2={} #Options to rolls
        
        for key, values in state_1.items():
            for value in values:
                if not value in state_2:
                    state_2[value]=[]
                    possible_rolls = list(combinations_with_replacement([1,2,3,4,5,6], 5-len(value)))
                    for roll in possible_rolls:
                        state_2[value].append(tuple(sorted(list(value)+list(roll))))
                    
        state_3 = state_1 #Rolls to Options
        state_4 = state_2 #Options to rolls
        
        available = self.outer_graph.getNode(self.start_id).get_available_positions()
        state_5 ={} #Rolls to card marking
        first_yahtzee = self.outer_graph.getNode(self.start_id).get_yahtzee()
        for key in combos:
            ##Rules: if upper section is available, it must go in that section
            ##If not, it must go in 3 or 4 of a kind.
            ##If not, it can go in any other spot, scoring full points for full house, small straight, or LS
            ##And the regular amount of points otherwise
            if first_yahtzee and len(set(key))==1:
                if key[0] - 1 in available:
                    available = [key[0]-1]
                elif 7 in available:
                    available=[7]
                elif 6 in available:
                    available = [6]
            state_5[key]=available

            
        return[state_1, state_2, state_3, state_4, state_5]   
            
        
        
    def generate_expected_values(self):
        state_5 = self.inner_widget[4]
        expected_values = {}
        for key, values in state_5.items():
            yahtzee_bonus = len(set(key))==1 and self.outer_graph.getNode(self.start_id).get_yahtzee()
            for value in values:
                if value==0:
                    expected_values[(key, value)] = key.count(1)
                elif value==1:
                    expected_values[(key, value)] = key.count(2)*2
                elif value==2:
                    expected_values[(key, value)] = key.count(3)*3
                elif value==3:
                    expected_values[(key, value)] = key.count(4)*4
                elif value==4:
                    expected_values[(key, value)] = key.count(5)*5
                elif value==5:
                    expected_values[(key, value)] = key.count(6)*6
                elif value==6:
                    if key.count(1)>2 or key.count(2)>2 or key.count(3)>2 or key.count(4)>2 or key.count(5)>2 or key.count(6)>2:
                        expected_values[(key, value)] = sum(list(key))
                    else:
                        expected_values[(key, value)] = 0
                elif value==7:
                    if key.count(1)>3 or key.count(2)>3 or key.count(3)>3 or key.count(4)>3 or key.count(5)>3 or key.count(6)>3:
                        expected_values[(key, value)] = sum(list(key))
                    else:
                        expected_values[(key, value)] = 0
                elif value==8:
                    if len(set(key))==2:
                        most_common = max(set(key), key = key.count)
                        if key.count(most_common)==3:
                            expected_values[(key, value)] = 25
                        else:
                            expected_values[(key, value)] = 0
                    elif yahtzee_bonus:
                        expected_values[(key, value)] = 25
                    else:
                        expected_values[(key, value)] = 0
                elif value == 9:
                    ordered = sorted(set(key))
                    if len(ordered)<4:
                        expected_values[(key, value)] = 0
                    else:
                        counts = [i-j for i, j in zip(ordered[1:len(ordered)], ordered[0:len(ordered)-1])]
                        if counts.count(1)>2:
                            expected_values[(key,value)]=30
                        else:
                            expected_values[(key, value)]=0
                    if yahtzee_bonus:
                        expected_values[(key, value)]=30
                elif value == 10:
                    ordered = sorted(set(key))
                    if len(ordered)<5:
                        expected_values[(key, value)] = 0
                    else:
                        counts = [i-j for i, j in zip(ordered[1:len(ordered)], ordered[0:len(ordered)-1])]
                        if counts.count(1)>3:
                            expected_values[(key,value)]=40
                        else:
                            expected_values[(key, value)]=0    
                    if yahtzee_bonus:
                        expected_values[(key, value)]=40
                elif value==11:
                    if len(set(key))==1:
                        expected_values[(key, value)]=50
                    else:
                        expected_values[(key, value)]=0
                elif value==12:
                    expected_values[(key, value)]=sum(list(key)) 
                if yahtzee_bonus:
                    expected_values[(key, value)]=100+expected_values[(key, value)]
                    
        return expected_values
                    
                    


                

                    
        
    

#a = Widget(12, vertices[12], OuterGraph(key, vertices))

        