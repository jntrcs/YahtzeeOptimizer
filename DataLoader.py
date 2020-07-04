#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:48:48 2020

@author: jntrcs
"""

import pickle
from OuterGraph import OuterGraph
from Widget import Widget

 
# Step 2
with open('vertice_ints', 'rb') as file:
 
    # Step 3
    vertices = pickle.load(file)


 
# Step 2
with open('int_to_states', 'rb') as file:
 
    # Step 3
    key = pickle.load(file)
    

graph = OuterGraph(key, vertices)
test_widget = Widget(1, key[1], graph)
evs = test_widget.generate_expected_values()

for keys, vals in vertices.items():
    if 14 in vals:
        print(keys)
        
print(key[109])

bw = Widget(109, key[109], graph)
evs = bw.get_expected_values()