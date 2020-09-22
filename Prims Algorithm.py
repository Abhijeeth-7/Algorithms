def primsMST(adj, source, V, MST):
    """
    Parameters
    ----------
    adj : 2D Matrix
        Adjacency Matrix of the graph.
    source : int 
        source node.
    V : int 
        Number of vertices in the graph.
    MST : 2D matrix 
        Empty 2D matrix for storing the result.

    Returns
    -------
    MST : 2D matrix 
        Minimum Spanning tree of the given graph.

    """
    MST = [[0 for i in range(V)] for j in range(V)]
    minvertix = None
    mincost = 10*9
    processed = [False for i in range(V)]
    processed_nodes = 0
    
    #initally source node is processed
    processed[source] = True
    processed_nodes += 1 
    
    # we keep constructing the tree. until we have processed all the nodes in the graph.
    while (processed_nodes != V):
        # from every node(processed node) in the Tree, check for the next minimum node. 
        for source in range(V):
            if not processed[source]:
                continue
            for dest in range(V):
                if (adj[source][dest]!=0 and not processed[dest]):
                    if (adj[source][dest]<mincost):
                        parent = source
                        minvertix = dest
                        mincost = adj[source][dest]
        # Add the minimum node to the MST Adjacency Matrix
        # consider the node as processed and increment the node count
        MST[parent][minvertix] = MST[minvertix][parent] = mincost
        processed[minvertix] = True
        processed_nodes += 1
        # reset the mincost ,To find next Min Node.
        mincost = 10*9
    
    return MST

if __name__=="__main__":
    adj =  [[0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]]
    
    MST = primsMST(adj,0,len(adj),list())
    print(*MST,sep='\n')