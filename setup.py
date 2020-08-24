#!/usr/bin/env python

from __future__ import print_function

import os
import platform
from setuptools import find_packages
from setuptools import setup
import subprocess
import sys


def get_data_files():

    def get_completion_install_location(shell):
        uname = platform.uname()[0]
        is_root = (os.geteuid() == 0)
        prefix = ''
        if is_root:
            # this is system install
            if uname == 'Linux' and shell == 'bash':
                prefix = '/'
            elif uname == 'Linux' and shell == 'zsh':
                prefix = '/usr/local'
            elif uname == 'Darwin' and shell == 'bash':
                prefix = '/'
            elif uname == 'Darwin' and shell == 'zsh':
                prefix = '/usr'
        if shell == 'bash':
            location = os.path.join(prefix, 'etc/bash_completion.d')
        elif shell == 'zsh':
            location = os.path.join(prefix, 'share/zsh/site-functions')
        else:
            raise ValueError('unsupported shell: {0}'.format(shell))
        return location

    loc = {'bash': get_completion_install_location(shell='bash'),
           'zsh': get_completion_install_location(shell='zsh')}
    files = dict(bash=['completion/pycd-completion.bash',
                       'completion/pypack-completion.bash'],
                 zsh=['completion/pycd-completion.bash',
                      'completion/_pycd', 'completion/_pypack'])
    data_files = []
    data_files.append((loc['bash'], files['bash']))
    data_files.append((loc['zsh'], files['zsh']))
    return data_files


__version__ = '0.3.30'


# publish helper
if sys.argv[-1] == 'publish':
    for cmd in ['python setup.py sdist upload',
                'git tag %s' % __version__,
                'git push origin master --tag']:
        subprocess.check_call(cmd, shell=True)
    sys.exit(0)

setup(
    name='pycd',
    version=__version__,
    packages=find_packages(),
    description='Tool to change directory for python modules.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='Kentaro Wada',
    author_email='www.kentaro.wada@gmail.com',
    url='http://github.com/wkentaro/pycd',
    install_requires=open('requirements.txt').readlines(),
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
    test_suite='nose.collector',
)
