import igraph as ig

def cluster_degree_betweenness(graph):
    """
    Implements the Smith-Pittman algorithm for community detection.
    
    Args:
        graph (igraph.Graph): Input graph.
    
    Returns:
        dict: A dictionary containing the results:
              - modularity scores
              - best community membership
              - iteration with highest modularity
    """
    # Step 1: Copy the graph to avoid modifying the original
    graph_ = graph.copy()
    
    # Step 2: Initialize containers
    modularities = []  # Store modularity values
    components = []    # Store community memberships

    # Step 3: Start the algorithm
    while len(graph_.es) > 0:
        # Identify the node with the highest degree centrality
        degree_centralities = graph_.degree()
        highest_degree_node = graph_.vs[degree_centralities.index(max(degree_centralities))]
        
        # Get all edges connected to this node
        connected_edges = graph_.incident(highest_degree_node, mode="all")
        
        # Calculate edge betweenness for all edges in the graph
        edge_betweenness = graph_.edge_betweenness()
        
        # Find the edge with the highest betweenness connected to the node
        highest_btwn_edge = max(connected_edges, key=lambda edge: edge_betweenness[edge])
        
        # Remove the edge with the highest betweenness
        graph_.delete_edges(highest_btwn_edge)
        
        # Remove isolated vertices (nodes with degree 0)
        isolated_vertices = [v.index for v in graph_.vs if v.degree() == 0]
        graph_.delete_vertices(isolated_vertices)

        # Calculate modularity for the current graph components
        current_components = graph_.components()
        current_modularity = graph_.modularity(current_components)
        
        # Store modularity and components
        modularities.append(current_modularity)
        components.append(current_components.membership)
    
    # Find the iteration with the highest modularity
    best_iteration = modularities.index(max(modularities))
    best_membership = components[best_iteration]
    
    # Prepare the results
    result = {
        "modularity": modularities,
        "membership": best_membership,
        "best_iteration": best_iteration
    }
    
    return result
