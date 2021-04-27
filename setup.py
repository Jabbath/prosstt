import os

from setuptools import setup, find_packages


setup(
    name="prosstt",
    version="1.2.0",
    packages=find_packages(),
    # scripts=['say_hello.py'],

    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib', 'newick'],
    python_requires=">=3.5",
    # metadata
    author="Nikolaos Papadopoulos, Johannes Soeding",
    author_email="npapado@mpibpc.mpg.de",
    description="Probabilistic simulation of single-cell RNA-seq tree-like topologies.",
    license="GPL3",
    keywords="single-cell RNA sequencing simulation probabilistic tree",
    url="https://github.com/soedinglab/PROSSTT",
    test_suite="nose.collector"
)
