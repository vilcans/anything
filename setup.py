#!/usr/bin/env python

from setuptools import setup 

with open('README.rst') as file:
    long_description = file.read()

setup(
    name='anything',
    version='0.1.0',
    description=(
        'A Python constant that considers itself equal to everything else. '
        'Useful for unit testing and more.'
    ),
    author='Martin Vilcans',
    author_email='martin@librador.com',
    url='https://github.com/vilcans/anything',
    py_modules=['anything'],
    license='MIT',
    keywords='unittest',
    long_description=long_description,
)
