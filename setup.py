#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.geoplanet',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.geoplanet'],
    version='0.03',
    description='Simple Python wrapper for Who\'s On First GeoPlanet-related functions',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-geoplant',
    install_requires=[
        "mapzen.whosonfirst.names"
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-names/tarball/master#egg=mapzen.whosonfirst.names-0.01',
        ],
    packages=packages,
    scripts=[
        'scripts/wof-append-geoplanet-names'
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-geoplanet/releases/tag/v0.03',
    license='BSD')
