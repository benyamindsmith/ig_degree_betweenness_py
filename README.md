# ig_degree_betweenness_py

Python implementation of the Smith-Pittman Algorithm available in the [`ig.degree.betweenness`](https://github.com/benyamindsmith/ig.degree.betweenness/) R package.

Unlike the R package which is more graphical. The python implementation preforms and outputs identified communities in the command line.

# Installation

```sh
pip install git+https://github.com/benyamindsmith/ig_degree_betweenness_py.git
```
# Usage

```sh
# for an undirected graph (default)
$ python ig_degree_betweenness.py my_edges.txt

# for a directed graph
$ python ig_degree_betweenness.py -d my_edges.txt

```