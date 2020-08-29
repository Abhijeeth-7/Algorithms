# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:28:31 2020

@author: kanch
"""
import sys

def floyd(adj):
    V=len(adj)
        
    for inter in range(V):
        for source in range(V):
            for dest in range(V):
                if adj[source][dest]!=0 and \
                adj[source][dest]>(adj[source][inter]+adj[inter][dest]):
                    adj[source][dest]=adj[source][inter]+adj[inter][dest]
    
    print(' ',*range(V),sep='\t')
    print('-------------------------------------')
    for i in range(V):
        print(i,end='|\t')
        for j in range(V):
            if adj[i][j]==sys.maxsize:
                adj[i][j]=-1
            print(adj[i][j],end='\t')
        print('\n-------------------------------------')
        
adj=[[0,5,sys.maxsize,10], 
             [sys.maxsize,0,3,sys.maxsize], 
             [sys.maxsize, sys.maxsize, 0,   1], 
             [sys.maxsize, sys.maxsize, sys.maxsize, 0] 
        ] 
#provide the ajacency matricx as an argument 
floyd(adj)