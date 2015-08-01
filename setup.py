#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import os
import sys
import imp
import subprocess
import platform
from setuptools import setup, find_packages


def get_version():
    try:
        file_, path, desc = imp.find_module('__version__', ['src/pycd'])
        version = imp.load_module('__version__', file_, path, desc).version
    finally:
        if file_ is not None:
            file_.close()
    return version


def get_data_files():

    def get_completion_install_location(shell):
        uname = platform.uname()[0]
        is_root = (os.geteuid() == 0)
        prefix = ''
        if shell == 'bash':
            if is_root and uname == 'Linux':
                prefix = '/'
            location = os.path.join(prefix, 'etc/bash_completion.d')
        elif shell == 'zsh':
            location = os.path.join(prefix, 'share/zsh/site-functions')
        else:
            raise ValueError('unsupported shell: {0}'.format(shell))
        return location

    location = {
        'bash': get_completion_install_location(shell='bash'),
        'zsh': get_completion_install_location(shell='zsh'),
        }
    comp_files = {
        'bash': [
            'completion/pycd-completion.bash',
            'completion/pypack-completion.bash',
            ],
        'zsh': [
            'completion/pycd-completion.bash',
            'completion/_pycd',
            'completion/_pypack',
            ],
        }
    data_files = [(location['bash'], comp_files['bash']),
                  (location['zsh'], comp_files['zsh'])]
    return data_files


# publish helper
if sys.argv[-1] == 'publish':
    for cmd in [
            'python setup.py sdist upload',
            'git tag {}'.format(get_version()),
            'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

long_desc = ('Simple command line tool to change directory'
             ' for python modules. You can now easily read'
             ' the codes of the modules.')
setup(
    name='pycd',
    version=get_version(),
    package_dir={'': 'src'},
    packages=find_packages('src'),
    description='Tool to change directory for python modules.',
    long_description=long_desc,
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/pycd',
    install_requires=['clint'],
    license='MIT',
    keywords='utility',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Topic :: Internet :: WWW/HTTP',
        ],
    entry_points={'console_scripts': ['pypack=pycd.cli:main']},
    scripts=['pycd.sh'],
    data_files=get_data_files(),
    )
