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
    
    def generate_FEVs(self):
        done_list = []
        FEVs = {}
        for k, v in self.vertices.items():
            if len(v)==0:
                done_list.append(k)
                FEVs[k]=0
                
        while(len(done_list)<len(vertices)):
            for k, v in vertices.items():
                if all(elem in done_list  for elem in v):
                    FEVs[k] = Widget(k, self.vertices[k], self).process()
                    done_list.append(k)
                    