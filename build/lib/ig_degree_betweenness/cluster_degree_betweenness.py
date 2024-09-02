import igraph as ig
import numpy as np

# Algorithm function, don't forget to comment out print()
def cluster_degree_betweenness(graph):
    
    # Name nodes and edges by original vertices
    #graph = g 
    graph.vs['name'] = ['node_{}'.format(i) for i in range(1, len(graph.vs)+1)]
    graph_ = graph.copy()  
    n_edges = len(graph_.es)  
    cmpnts = []  # To store components at each step
    modularities = []
    #subgraph_cmpnts = []
    
    for i in range(n_edges-1):
        try:
            # Sort the nodes by degree in descending order
            degree_nodes = sorted(graph_.vs['name'], key=lambda x: graph_.degree(x), reverse=True)
            
            # Calculate edge betweenness
            edgelist = [(graph_.vs[edge.source]['name'], graph_.vs[edge.target]['name']) for edge in graph_.es]
            graph_.es['name'] = edgelist
            #len(edgelist)
            edge_btwn = dict(zip(edgelist, graph_.edge_betweenness())) #Python dictionary can't have duplicate keys
            #len(edge_btwn)
            
            # Create subgraph of edges associated with the highest-degree node
            node = degree_nodes[0]
            edges_to_keep = [index for index, item in enumerate(edgelist) if str(node) in item]
            subgraph = graph_.subgraph_edges(edges_to_keep, delete_vertices=True)
            #ig.summary(subgraph)
            #print(subgraph)
            
            # If subgraph has no edges, store the components and continue
            if len(subgraph.es) == 0:  
                cmpnts.append(graph_.components())
                continue
            
            # Calculate edge betweenness for the subgraph and find the edge with the highest betweenness
            subgraph_edgelist = [(subgraph.vs[edge.source]['name'], subgraph.vs[edge.target]['name']) for edge in subgraph.es]
            #len(subgraph_edgelist)
            subgraph_edge_betweeness = sorted([edge for edge in subgraph_edgelist if edge in edge_btwn], 
                                              key=lambda x: edge_btwn[x], reverse=True)
            #len(subgraph_edge_betweeness)
            
            # Remove the edge with the highest betweenness
            edge_to_delete = graph_.es.find(name_eq=subgraph_edge_betweeness[0])  
            graph_.delete_edges(edge_to_delete)
            
            # Find vertices with degree 0
            isolated_vertices = [v.index for v in graph_.vs if graph_.degree(v) == 0]
            
            # Remove isolated vertices
            graph_.delete_vertices(isolated_vertices)

            #ig.summary(graph_)
            #print(graph_)
            cmpnts.append(graph_.components())
            modularities.append(graph_.modularity(graph_.components()))
            #print(subgraph_edge_betweeness[0])
            #print(graph_.components())
            #subgraph_cmpnts.append(graph_.copy())
            #print(i)
        except :
            break
    
    # Calculate modularity for each component
    communities = [cmp.membership for cmp in cmpnts]      
    
    # Find the iteration with the highest modularity
    iter_num = modularities.index(max(modularities))
    # Prepare the result
    res = {
        "names": graph.vs['name'],
        "vcount": graph.vcount(),
        "algorithm": "Smith-Pittman",
        "modularity": modularities,
        "membership": communities[iter_num]
    }
    
    return res