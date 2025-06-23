#!/usr/bin/env python3
import sys
import argparse
import igraph as ig

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run degree+betweenness clustering on an edge list."
    )
    parser.add_argument(
        "filename",
        help="Path to a tab-delimited edge-list file (one edge per line, e.g. u<TAB>v)."
    )
    parser.add_argument(
        "-d", "--directed",
        action="store_true",
        help="Treat the edge list as directed.  (Default: undirected)"
    )
    return parser.parse_args()

def community_degree_betweenness(graph):
    """
    Community Structure Detection Based on Node Degree Centrality and Edge Betweenness

    Referred to as the "Smith-Pittman" algorithm in Smith et al (2024). This algorithm detects communities by calculating the degree centrality measures of nodes and edge betweenness.

    The algorithm iteratively removes edges based on their betweenness centrality and the degree of their adjacent nodes. At each iteration, it identifies the edge with the highest betweenness centrality among those connected to nodes with the highest degree. It then removes that edge and recalculates the modularity of the resulting graph. This process continues until all edges have been assessed or until no further subgraph can be created with the optimal number of communites being chosen based on maximization of modularity.

    Args:
        graph (igraph.Graph): The input graph, which can be directed or undirected.
    Returns:
        igraph.VertexClustering: A clustering object containing the community structure of the graph.
    """
    # (unchanged body)
    graph_ = graph.copy()
    n_edges = len(graph_.es)
    n_nodes = len(graph_.vs)
    cmpnts = []
    modularities = []

    for i in range(n_edges):
        try:
            degree_nodes = sorted(
                graph_.vs["name"],
                key=lambda x: graph_.degree(x),
                reverse=True
            )

            edgelist = [
                (graph_.vs[e.source]["name"], graph_.vs[e.target]["name"])
                for e in graph_.es
            ]
            graph_.es["name"] = edgelist
            edge_btwn = dict(zip(edgelist, graph_.edge_betweenness()))

            node = degree_nodes[0]
            edges_to_keep = [
                idx for idx, (u, v) in enumerate(edgelist)
                if node == u or node == v
            ]
            subgraph = graph_.subgraph_edges(edges_to_keep, delete_vertices=True)
            if len(subgraph.es) == 0:
                cmpnts.append(graph_.components(mode="weak"))
                continue

            sub_el = [
                (subgraph.vs[e.source]["name"], subgraph.vs[e.target]["name"])
                for e in subgraph.es
            ]
            subgraph_edge_betweeness = sorted(
                [e for e in sub_el if e in edge_btwn],
                key=lambda x: edge_btwn[x],
                reverse=True
            )

            edge_to_delete = graph_.es.find(name_eq=subgraph_edge_betweeness[0])
            graph_.delete_edges(edge_to_delete)

            cmpnt = graph_.components(mode="weak")
            cmpnts.append(cmpnt)

            modal = graph.modularity(cmpnt.membership)
            modularities.append(modal)
            #print(f"Iteration {i+1}: modularity {modal:.4f}")

        except Exception:
            break

    # choose best iteration
    best_idx = modularities.index(max(modularities))
    best_membership = cmpnts[best_idx].membership

    # summary
    # print(f"\nSummary:")
    # print(f"  Number of nodes: {n_nodes}")
    # print(f"  Number of edges: {n_edges}")
    # print(f"  Best iteration: {best_idx+1}")
    # print(f"  Max modularity: {max(modularities):.4f}")
    # print(f"  Communities found: {len(set(best_membership))}")
    # print(f"  Membership vector: {best_membership}")
    # print(f"  Node names: {graph.vs['name']}")

    # bridges
    # bridges = graph.bridges()
    # bridge_nodes = [
    #     (graph.vs[e[0]]["name"], graph.vs[e[1]]["name"])
    #     for e in (graph.es[i].tuple for i in bridges)
    # ]

    # return {
    #     "names": graph.vs["name"],
    #     "vcount": graph.vcount(),
    #     "algorithm": "node degree+edge betweenness",
    #     "modularity": modularities,
    #     "membership": best_membership,
    #     "bridges": bridge_nodes
    # }
    return ig.clustering.VertexClustering(graph, membership=best_membership)


def main():
    args = parse_args()

    # Read edges
    with open(args.filename, "r") as f:
        edges = [tuple(line.strip().split("\t")) for line in f]

    # Build graph with directed flag
    g = ig.Graph.TupleList(edges, directed=args.directed)

    # Compute clustering
    result = community_degree_betweenness(g)
    print(result)

if __name__ == "__main__":
    main()
