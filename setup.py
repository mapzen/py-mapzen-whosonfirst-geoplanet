#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.geoplanet',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.geoplanet'],
    version='0.02',
    description='Simple Python wrapper for Who\'s On First GeoPlanet-related functions',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-geoplant',
    install_requires=[
        "mapzen.whosonfirst.labels"
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-append-geoplanet-names'
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-geoplanet/releases/tag/v0.02',
    license='BSD')
