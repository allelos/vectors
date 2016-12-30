import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="vectors",
    version="0.0.9",
    author="Pantelis Paliagkas",
    author_email="p.paliagkas@gmail.com",
    description="A simple vector toolkit dealing with vectors and points \
        in the 3-dimensional space",
    long_description=read('README.rst'),
    license="The MIT License (MIT)",
    url="https://github.com/allelos/vectors",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
