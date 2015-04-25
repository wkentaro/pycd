#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import os
import sys
from setuptools import setup, find_packages


if sys.version_info < (2, 7):
    print('pycd requires python version >= 2.7.', file=sys.stderr)
    sys.exit(1)

install_requires = ['clint==0.4.1']


# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


long_desc = """Simple command line tool to change directory
for python modules. You can now easily read the codes of the modules."""
version='0.1.21'


setup(
    name="pycd",
    version=version,
    description="Tool to change directory for python modules.",
    long_description=long_desc,
    author="Kentaro Wada",
    author_email='www.kentaro.wada@gmail.com',
    url="http://github.com/wkentaro/pycd",
    install_requires=install_requires,
    packages=find_packages(),
    package_data={'pycd': ['pycd.sh']},
    license="MIT",
    keywords="utility",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
    ],
    entry_points={
        'console_scripts': [
            'pycd_py = pycd.cli:main',
        ],
    }
)
