#!/usr/bin/env python

from setuptools import setup, find_packages

version = '1.0.0'

required = open('requirements.txt').read().split('\n')

setup(
    name='tuning',
    version=version,
    description='compute linear and nonlinear tuning curves',
    author='freeman-lab',
    author_email='the.freeman.lab@gmail.com',
    url='https://github.com/freeman-lab/tuning',
    packages=find_packages(),
    install_requires=required,
    long_description='See ' + 'https://github.com/freeman-lab/tuning',
    license='MIT'
)
