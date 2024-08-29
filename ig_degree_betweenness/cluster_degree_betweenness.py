import igraph as ig
import numpy as np

def cluster_degree_betweenness(graph):
 graph_ = graph.copy() # Create a copy of the graph
 n_edges = len(graph_.es) # Get the number of edges
 cmpnts = [] # To store components at each step
 for i in range(n_edges):
   # Sort the nodes by degree in decreasing orde
   degree_nodes = sorted(graph_.vs['name'], key=lambda x: graph_.degree(x), reverse=True)
   # Create an edge list and calculate edge betweenness
   edgelist = ["|".join(str(sorted(edge.tuple))) for edge in graph_.es]
   edge_btwn = dict(zip(edgelist, graph_.edge_betweenness()))
   # Create subgraph of edges associated with the highest-degree node
   node = degree_nodes[0]
   subgraph = graph_.subgraph_edges(graph_.es.select(_source_in=[node], _target_in=[node]), delete_vertices=True)
   if len(subgraph.es) == 0: # If subgraph has no edges, store the components and continue
     cmpnts.append(graph_.components())
     continue
   # Calculate edge betweenness for the subgraph and find the edge with the highest betweenness
   subgraph_edgelist = ["|".join(sorted(edge.tuple)) for edge in subgraph.es]
   subgraph_edge_betweeness = sorted([edge for edge in subgraph_edgelist if edge in edge_btwn],key=lambda x: edge_btwn[x], reverse=True)
   # Remove the edge with the highest betweenness
   graph_.delete_edges([subgraph_edge_betweeness[0]])
   cmpnts.append(graph_.components())
   # Calculate modularity for each component
   communities = [cmp.membership for cmp in cmpnts]
   modularities = [graph.modularity(community) for community in communities]
   # Find the iteration with the highest modularity
   iter_num = np.argmax(modularities)
   # Prepare the result
   res = {
     "names": graph.vs['name'],
     "vcount": graph.vcount(),
     "algorithm": "Smith-Pittman",
     "modularity": modularities,
     "membership": communities[iter_num]
     }
  return res


