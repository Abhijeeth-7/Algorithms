# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:30:18 2020

@author: kanch
"""
import sys

def bellmanford(adj,source):
    N=len(adj)
    edges=list()
    dist=[sys.maxsize]*N
    dist[0]=0
    
    class edge:
        def __init__(self,u,v,weight):
            self.source=u
            self.dest=v
            self.weight=weight 
            
    for u in range(len(adj)):
        for v in range(len(adj)):
            if adj[u][v]!=0:
                new_edge = edge(u,v,adj[u][v])
                edges.append(new_edge)
    
    for _ in range(len(adj)-1):
        for edge in edges:
            if dist[edge.source]!=0 and \
            dist[edge.dest] > dist[edge.source]+edge.weight:
                dist[edge.dest]=dist[edge.source]+edge.weight
                
#   checking for negative cycles
#   if the distances are reduced even further after bellmanford algorithm
#   it indicates the presence of negative cycles             
    for edge in edges:
        if dist[edge.source]!=9999 and\
        dist[edge.dest] > dist[edge.source]+edge.weight:
            print("""negative cycles in the graph!,
                  can't run this algorithm on graph 
                  with negative cycles""")
            break
    else:
        print(*range(N))
        print(*dist)
        


adj=[[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ]; 
#provide adjacency matrix and source as arguments
bellmanford(adj,0)            
                