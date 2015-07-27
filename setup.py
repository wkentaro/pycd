#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import os
import sys
import imp
from setuptools import setup, find_packages


if sys.version_info < (2, 7):
    print('pycd requires python version >= 2.7.', file=sys.stderr)
    sys.exit(1)

def get_version():
    try:
        ver_file, pathname, description = imp.find_module('__version__', ['pycd'])
        vermod = imp.load_module('__version__', ver_file, pathname, description)
        version = vermod.version
        return version
    finally:
        if ver_file is not None:
            ver_file.close()

# Publish Helper.
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

long_desc = """Simple command line tool to change directory
for python modules. You can now easily read the codes of the modules."""
version=get_version()
install_requires = ['clint==0.4.1']

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
            'pypkg = pycd.cli:main',
        ],
    }
)
