#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 21:06:40 2020

@author: jntrcs
"""

class OuterGraph:
    def __init__(self):
        print("hi")
        
    def __init__(self, key, vertices):
        self.key = key
        self.vertices = vertices
        
    def getNode(self, integer):
        return(self.key[integer])