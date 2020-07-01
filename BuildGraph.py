#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 15:35:03 2020

@author: jntrcs
"""

from GameState import GameState
import pickle

####Generate all possible vertices from one game card to another




def findVertices(state, vertices):
    vertices[state] = []
    top = state.get_top()
    for i in range(6):
        if not top[i]:
            for score in range(6):
                vertices[state].append(state.mark_top(i+1, (score)*(i+1)))
    
    bottom = state.get_bottom()
    for i in range(7):
        if not bottom[i]:
            vertices[state].append(state.mark_bottom(i))
            if i ==6:
               vertices[state].append(state.mark_bottom(i, True))
    return vertices




def check_self_and_all_children(state, vertices, checked):
    if state in checked:
        return vertices, checked
    vertices = findVertices(state, vertices)
    checked[state]=True
    for i in vertices[state]:
        vertices, checked = check_self_and_all_children(i, vertices, checked)
    return vertices, checked


new_game =  GameState()


vertices = {}
checked = {}
        
vertices, checked = check_self_and_all_children(new_game, vertices, checked)


with open('vertices', 'wb') as vertice_file:
      pickle.dump(vertices, vertice_file)
      
print("done")
