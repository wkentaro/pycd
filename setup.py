#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
from __future__ import print_function
import sys
import imp
import subprocess
import platform
from setuptools import setup, find_packages


def get_version():
    try:
        file_, path, desc = imp.find_module('__version__', ['pycd'])
        version = imp.load_module('__version__', file_, path, desc).version
    finally:
        if file_ is not None:
            file_.close()
    return version


def get_data_files():
    uname = platform.uname()[0]
    if uname == 'Linux':
        prefix = '/'
    else:  # for Darwin and other platforms
        prefix = ''
    bash_comp_loc = prefix + 'etc/bash_completion.d'
    zsh_comp_loc = 'share/zsh/site-functions'

    # we expect each completion script to be installed in
    # wstool-completion.bash:
    #   - /etc/bash_completion.d (Linux)
    #   - /usr/local/share/bash_completion.d (Darwin)
    # _wstool:
    #   - /usr/local/share/zsh/site-functions (Linux and Darwin)
    data_files = [
        (bash_comp_loc, ['completion/pycd-completion.bash']),
        (zsh_comp_loc, ['completion/_pycd', 'completion/_pypkg']),
        ]
    return data_files


def main():
    version = get_version()

    # publish helper
    if sys.argv[-1] == 'publish':
        for cmd in [
                'python setup.py sdist upload',
                'git tag {}'.format(version),
                'git push origin master --tag']:
            subprocess.check_call(cmd, shell=True)
        sys.exit(0)

    long_desc = ('Simple command line tool to change directory'
                 ' for python modules. You can now easily read'
                 ' the codes of the modules.')
    setup(
        name='pycd',
        version=version,
        description='Tool to change directory for python modules.',
        long_description=long_desc,
        author='Kentaro Wada',
        author_email='www.kentaro.wada@gmail.com',
        url='http://github.com/wkentaro/pycd',
        install_requires=['clint>=0.4.1'],
        packages=find_packages(),
        license='MIT',
        keywords='utility',
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX',
            'Topic :: Internet :: WWW/HTTP',
            ],
        entry_points={'console_scripts': ['pypkg = pycd.cli:main']},
        scripts=['pycd.sh'],
        data_files=get_data_files(),
    )


if __name__ == '__main__':
    main()
