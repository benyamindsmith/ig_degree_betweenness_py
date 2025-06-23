import igraph as ig
from ig_degree_betweenness import community_degree_betweenness
import matplotlib.pyplot as plt
import matplotlib

# Use non-interactive backend (important for CI/testing)
matplotlib.use("Agg")


def test_community_degree_betweenness_basic_graph():
    # Define a small test graph directly
    edges = [
        ("A", "B"),
        ("B", "C"),
        ("C", "D"),
        ("D", "A"),
        ("A", "C"),  # Add some extra structure
        ("E", "F"),
        ("F", "G"),
        ("G", "E")   # A second small cycle (community)
    ]

    # Build the graph
    g = ig.Graph.TupleList(edges, directed=True)

    # Run the community detection
    clustering = community_degree_betweenness(g)

    # Assertions
    assert clustering is not None
    assert hasattr(clustering, "__len__")
    assert len(clustering) >= 1  # At least one community

    # Optional: check that vertices are assigned to communities
    memberships = clustering.membership
    assert len(memberships) == g.vcount()

    # Plot to file to ensure plotting works (no GUI)
    fig, ax = plt.subplots()
    ig.plot(
        clustering,
        target=ax,
        mark_groups=True,
        vertex_size=15,
        edge_width=0.5,
    )
    fig.set_size_inches(8, 8)
    fig.savefig("test_output_plot.png")
    plt.close(fig)
