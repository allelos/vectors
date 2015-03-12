import os

from setuptools import setup, find_packages

setup(
    name = "vectors",
    version = "0.0.8",
    author = "Allelos",
    author_email = "p.paliagkas@gmail.com",
    description = "A simple vector toolkit dealing with vectors and points \
        in the 3-dimensional space",
    license = "The MIT License (MIT)",
    url = "https://github.com/allelos/vectors",
    packages = find_packages(),
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
