#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 21:48:48 2020

@author: jntrcs
"""

import pickle

 
# Step 2
with open('vertice_ints', 'rb') as file:
 
    # Step 3
    vertices = pickle.load(file)


 
# Step 2
with open('int_to_states', 'rb') as file:
 
    # Step 3
    key = pickle.load(file)