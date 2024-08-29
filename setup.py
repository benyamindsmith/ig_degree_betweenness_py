from setuptools import setup, find_packages

setup(
    name="ig_degree_betweenness",
    version="0.1",
    description="Implementation of the degree-betweenness community detection algortihm developed by Benjamin Smith and Tyler Pittman",
    packages=find_packages(),
    install_requires=[
        "igraph",
        "numpy"
    ],
)
