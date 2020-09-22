# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:42:36 2020

@author: kanch
"""

def getEdges(adj, V, edges):
    """
    returns the sorted list of edges from the graph.
    Each edge is repsented a a tuple in the following format:
        Edge(vertix1,vertix2, Weight of th Egde)
    """
    for i in range(V):
        for j in range(V):
            if adj[i][j]!=0:
                edges.append((i,j,adj[i][j]))
    
    edges.sort(key = lambda x: x[2])
    return edges

def parentInTree(node, parent, adj):
    """
    returns True if the parent of the given vertix is the MST tree,
    otherwise returns False.
    """
    while parent[node]!=None:
        if adj[parent[node]][node]!=0:
            return True
    return False

def krushkalMST(adj, V, MST):
    MST = [[0 for j in range(V)] for i in range(V)]
    parent = [None for i in range(V)]
    edges = getEdges(adj, V, list())
    
    for edge in edges:
        v1,v2,wt = edge[0],edge[1],edge[2]
        if parentInTree(v1,parent,adj) and parentInTree(v2,parent,adj):
            continue
        else:
            MST[v1][v2] = MST[v2][v1] = wt
            parent[v2] = v1
    return MST     
   
if __name__=="__main__":
    adj =  [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
    
    MST = krushkalMST(adj,len(adj),list())
    print(*MST,sep='\n') 