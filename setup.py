#!/usr/bin/env python

from distutils.core import setup

setup(name='libdw',
      version='2016',
      description='The Digital World Code Distribution',
      author='-',
      author_email='-',
      # url='https://www.python.org/sigs/distutils-sig/',
      py_modules = ['firebase'],
      packages = ['libdw','form','soar','soar.io','soar.graphics',\
                  'soar.serial','soar.controls','soar.outputs',\
                  'eBot','eBot.serial','firebase'],
      package_data={'libdw': ['*.pyc'], 'form': ['*.pyc'],\
                    'soar': ['*.pyc', 'io/*.pyc', 'graphics/*.pyc',\
                             'serial/*.pyc', 'controls/*.pyc', 'outputs/*.pyc',\
                             'media/*','worlds/*']},
      scripts=['setupsoar.py', 'soar/soar']
     )

