#!/usr/bin/env python

# Remove .egg-info directory if it exists, to avoid dependency problems with
# partially-installed packages (20160119/dphiffer)

import os, sys
from shutil import rmtree

cwd = os.path.dirname(os.path.realpath(sys.argv[0]))
egg_info = cwd + "/mapzen.whosonfirst.geoplanet.egg-info"
if os.path.exists(egg_info):
    rmtree(egg_info)

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read()
version = open("VERSION").read()

setup(
    name='mapzen.whosonfirst.geoplanet',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.geoplanet'],
    version=version,
    description='Simple Python wrapper for Who\'s On First GeoPlanet-related functions',
    author='Mapzen',
    url='https://github.com/whosonfirst/py-mapzen-whosonfirst-geoplant',
    install_requires=[
        "mapzen.whosonfirst.names>=0.02"
        ],
    dependency_links=[
        'https://github.com/whosonfirst/py-mapzen-whosonfirst-names/tarball/master#egg=mapzen.whosonfirst.names-0.02',
        ],
    packages=packages,
    scripts=[
        'scripts/wof-append-geoplanet-names'
        ],
    download_url='https://github.com/whosonfirst/py-mapzen-whosonfirst-geoplanet/releases/tag/' + version,
    license='BSD')
