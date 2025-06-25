# ig_degree_betweenness_py

[![PyPI - Version](https://img.shields.io/pypi/v/ig-degree-betweenness)](https://pypi.org/project/ig-degree-betweenness/)
[![Pepy Total Downloads](https://img.shields.io/pepy/dt/ig-degree-betweenness)](https://pepy.tech/projects/ig-degree-betweenness)
[![arXiv](https://img.shields.io/badge/arXiv-2411.01394-b31b1b.svg)](https://arxiv.org/abs/2411.01394)


Python implementation of the Smith-Pittman Algorithm available in the [`ig.degree.betweenness`](https://github.com/benyamindsmith/ig.degree.betweenness/) R package.

This code can be used both as a standard Python library for scripting and as a command-line tool.

<a> 
<img src='https://github.com/benyamindsmith/ig.degree.betweenness/assets/46410142/37f82c83-1600-4e9f-913e-5e43bbe90427', height = "300"/>
</a>


<a> 
<img src='https://github.com/user-attachments/assets/63187b8f-58af-4c08-8b80-8a31b945899a' height = "610"/>
</a>

# Installation

To install from PyPI, run:

```sh
pip install ig-degree-betweenness
```

To install from GitHub, run. 

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
$ python ig_degree_betweenness my_edges.txt

# for a directed graph
$ python ig_degree_betweenness -d my_edges.txt

```
