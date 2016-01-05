#!/usr/bin/env python

from setuptools import setup

setup(
    name='tildenet',
    version='0.0.0',
    description='weird social network for interesting people',
    url='https://github.com/tildetown/tildenet',
    author='vilmibm shaksfrpease',
    author_email='nathanielksmith@gmail.com',
    license='AGPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU Affero General Public License v3',
    ],
    keywords='social',
    packages=['tildenet'],
    install_requires = ['peewee==2.7.4',],
)
