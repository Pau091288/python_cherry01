# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from python_cherry01 import __version__


setup(
    name="python_cherry01",
    version=__version__,
    description="CherryPy based microservice.",
    maintainer="",
    packages=["python_cherry01"],
    platforms=["any"]
)
