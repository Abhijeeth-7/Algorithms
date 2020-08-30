# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:24:35 2020

@author: kanch
"""
import sys 

def getPath(dest,path):
    if path[dest] is None:
        print(dest,end='->')
        return 
    getPath(path[dest],path)
    print(dest,end='->')

def Dijikstra(V,source,dest):
    considered=[0]*V
    dist=[sys.maxsize]*V
    prevNode=[source]*V
    processedNodes=0
    
    dist[source]=0
    prevNode[source]=None
    processedNodes+=1
    while processedNodes!=V:
#       selecting next node to be proccessed 
        nextNode=None
        for i in range(V):
            if not considered[i]:
                if nextNode == None:
                    nextNode = i
                if dist[nextNode] > dist[i]: 
                    nextNode = i
#       considering in the list of selected nodes 
        considered[nextNode]=1
        processedNodes+=1
#      Updating the distances/weights based on the selected node.
#      Only if the newly discoved distance is lesser than previous distance
        for j in range(V):
            if adj[nextNode][j]!=0 and not considered[j] \
                and (dist[nextNode]+adj[nextNode][j])<dist[j]:
                    dist[j]=dist[nextNode]+adj[nextNode][j]
                    prevNode[j]=nextNode
    print(*range(V))
    print(*dist)
    print("~path from source to destination~")
    getPath(dest,prevNode)

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
#please provide the arguments in the following manner:
# arg1: adj matrix
# arg2: Soruce vertix
# arg3: Destination
Dijikstra(len(adj),0,8)            
