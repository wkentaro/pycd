#!/bin/sh
#

function _get_dist_path()
{
python -c """
import os
import sys
import argparse
import imp
import pkgutil

def get_distribution_paths():
    pkg_paths = {}
    for pkg in pkgutil.iter_modules():
        pkg_name = pkg[1]
        file_, pkg_path = imp.find_module(pkg_name)[:2]
        pkg_dirname = os.path.split(pkg_path)[0]
        if file_ is None:
            pkg_paths[pkg_name] = pkg_path
        else:
            pkg_paths[pkg_name] = pkg_dirname
    return pkg_paths

def main():
    if len(sys.argv) < 2:
        print('usage: pycd DIST_NAME')
        return
    dist_paths = get_distribution_paths()
    try:
        dist_path = dist_paths[sys.argv[1]]
    except KeyError:
        print('package not found: %s' % sys.argv[1])
        return
    print(dist_path)

main()
""" $1
}

function pycd ()
{
  DIST_PATH=`_get_dist_path $1`
  # change dir or print warning or usage
  cd $DIST_PATH &>/dev/null || echo $DIST_PATH
}