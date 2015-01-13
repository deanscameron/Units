""" Setup file for Units"""

from setuptools import setup, find_packages

setup(
    name = "Units",
    version = "0.1",
    packages = find_packages(exclude=['*test']),
    )