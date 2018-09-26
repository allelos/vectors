from setuptools import setup, find_packages
from codecs import open
from os import path

cwd = path.abspath(path.dirname(__file__))
with open(path.join(cwd, 'README.md')) as f:
    long_description = f.read()

setup(
    name="vectors",
    version="1.0.0",
    author="Pantelis Paliagkas",
    author_email="p.paliagkas@gmail.com",
    description="A simple vector toolkit dealing with vectors and points \
        in the 3-dimensional space",
    long_description=long_description,
    license="The MIT License (MIT)",
    url="https://github.com/allelos/vectors",
    packages=find_packages(exclude=['contrib', 'docs', 'test']),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
