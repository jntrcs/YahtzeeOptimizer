#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 14:51:24 2020

@author: jntrcs
"""

import copy

class GameState:
    def __init__(self):
        self.top=[False]*6
        self.top_score = 0
        self.bottom = [False]*7
        self.yahtzee = False
        

        
    def get_top(self):
        return self.top;
    
    def get_top_score(self):
        return self.top_score;
    
    def get_bottom(self):
        return self.bottom
    
    def get_yahtzee(self):
        return self.yahtzee;
    
    def __hash__(self):
        return hash(str(self))
    
    def __str__(self):
        return "Top: " + str(self.top)+"\nTop Score: "+str(self.top_score)+"\nBottom: " + str(self.bottom) + "\nYahtzee: "+ str(self.yahtzee)

    def __eq__(self, other):
        if (self.top == other.get_top() and
               self.top_score == other.get_top_score() and
               self.bottom == other.get_bottom() and
               self.yahtzee == other.get_yahtzee()):
                  return True
        return False
    
    def mark_top(self, number, scored):
        new_card = copy.deepcopy(self)
        new_card.update_top(number, scored)
        return new_card
    
    def update_top(self, number, scored):
        self.top[number-1] = True
        self.top_score = self.top_score + scored
        if self.top_score>63:
            self. top_score = 63
            
    def mark_bottom(self, which, got_yahtzee=False):
        new_card = copy.deepcopy(self)
        new_card.update_bottom(which, got_yahtzee)
        return new_card
    
    def update_bottom(self, which, got_yahtzee=False):
        self.bottom[which] = True 
        if which == 5:
            if got_yahtzee:
                self.yahtzee=True
                
    def get_available_positions(self):
        
        return([i for i, val in enumerate(self.top) if not val] + [i+6 for i, val in enumerate(self.bottom) if not val])
    