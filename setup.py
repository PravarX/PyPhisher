#!/usr/bin/env python

from setuptools import setup

version = open("files/version.txt").read().strip()
long_description = open("README.md").read().strip()

setup(
    name='PyPhisher',
    version=version,
    description='Ultimate phishing tool in python with dual tunneling, 77 templates and many more!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='PravarNotFound',
    author_email='PravarX@gmail.com',
    license="GPLv3",
    url='https://github.com/PravarX/PyPhisher/',
    scripts=['pyphisher'],
    install_requires=["requests", "bs4"]
)
