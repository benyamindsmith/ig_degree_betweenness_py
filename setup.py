from setuptools import setup, find_packages

DESCRIPTION = "Smith-Pittman Community Detection Algorithm for 'igraph' Objects (2024)"
LONG_DESCRIPTION = """
Implements the "Smith-Pittman" community detection algorithm for network analysis using 'igraph' objects. This algorithm combines node degree and betweenness centrality measures to identify communities within networks, with a gradient evident in social partitioning. The package provides functions for community detection, visualization, and analysis of the resulting community structure. Methods are based on results from Smith, Pittman and Xu (2024) <doi:10.48550/arXiv.2411.01394>.
"""
setup(
    name="ig_degree_betweenness",
    author='Benjamin Smith, Tyler Pittman, Wei Xu',
    author_email='benyamin.smith@mail.utoronto.ca, Tyler.Pittman@uhn.ca, Wei.Xu@uhn.ca',
    version="0.1.0",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=["python-igraph"],
    keywords=['igraph'],
        url='https://github.com/benyamindsmith/ig_degree_betweenness_py',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    project_urls={
        'Benjamin Smith ORCID': 'https://orcid.org/0009-0007-2206-0177',
        'Tyler Pittman ORCID': 'https://orcid.org/0000-0002-5013-6980',
        'Wei Xu ORCID': 'https://orcid.org/0000-0002-0257-8856'
    }
)
