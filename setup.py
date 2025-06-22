from setuptools import setup, find_packages

DESCRIPTION = "Smith-Pittman Community Detection Algorithm for 'igraph' Objects (2024)"
LONG_DESCRIPTION = open("README.md").read()
setup(
    name="ig_degree_betweenness",
    author='Benjamin Smith, Tyler Pittman, Wei Xu',
    author_email='benyamin.smith@mail.utoronto.ca, Tyler.Pittman@uhn.ca, Wei.Xu@uhn.ca',
    version="0.1.1",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown", 
    install_requires=["python-igraph"],
    license= "MIT",
    entry_points={
        "console_scripts": [
            "ig_degree_betweenness=ig_degree_betweenness:ig_degree_betweenness",
        ],
    },
    keywords=['igraph'],
        url='https://github.com/benyamindsmith/ig_degree_betweenness_py',
    packages=find_packages(),
    classifiers=[
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ],
    project_urls={
        'Benjamin Smith ORCID': 'https://orcid.org/0009-0007-2206-0177',
        'Tyler Pittman ORCID': 'https://orcid.org/0000-0002-5013-6980',
        'Wei Xu ORCID': 'https://orcid.org/0000-0002-0257-8856'
    }
)
