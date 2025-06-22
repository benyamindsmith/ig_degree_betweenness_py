# ig_degree_betweenness_py

Python implementation of the Smith-Pittman Algorithm available in the [`ig.degree.betweenness`](https://github.com/benyamindsmith/ig.degree.betweenness/) R package.

This code can be used both as a standard Python library for scripting and as a command-line tool.

<a> 
<img src='https://github.com/benyamindsmith/ig.degree.betweenness/assets/46410142/37f82c83-1600-4e9f-913e-5e43bbe90427', height = "300"/>
</a>



# Installation

```sh
pip install git+https://github.com/benyamindsmith/ig_degree_betweenness_py.git
```
# Usage

## Scripting Usage

To use this in a typical scripting setting compute the clustering with the following code. 

```python 
import igraph as ig
from ig_degree_betweenness import community_degree_betweenness
import matplotlib.pyplot as plt


# Read edges
with open("edgelist.txt", "r") as f:
    edges = [tuple(line.strip().split("\t")) for line in f]

# Build graph with directed flag
g = ig.Graph.TupleList(edges, directed=True)

# Compute clustering
sp_clustering = community_degree_betweenness(g)
```

This can be further visualized:

```py
# Visualize Communities
fig1, ax1 = plt.subplots()
ig.plot(
    sp_clustering,
    target=ax1,
    mark_groups=True,
    vertex_size=15,
    edge_width=0.5,
)
fig1.set_size_inches(20, 20)
```

![](./sp_communities_matplotlib.png)

To run this code in the terminal, run: 

## Terminal Usage

```sh
# for an undirected graph (default)
$ python ig_degree_betweenness.py my_edges.txt

# for a directed graph
$ python ig_degree_betweenness.py -d my_edges.txt

```
