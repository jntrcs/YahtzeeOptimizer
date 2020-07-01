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
        for key in combos:
            state_5[key]=available
        return[state_1, state_2, state_3, state_4, state_5]    
        