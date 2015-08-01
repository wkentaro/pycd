#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import imp
import pkgutil


def get_package_paths():
    pkg_paths = {}
    for pkg in pkgutil.iter_modules():
        pkg_name = pkg[1]
        try:
            file_, pkg_path = imp.find_module(pkg_name)[:2]
        except ImportError:
            continue
        pkg_dirname = os.path.split(pkg_path)[0]
        if file_ is None:
            pkg_paths[pkg_name] = os.path.abspath(pkg_path)
        else:
            pkg_paths[pkg_name] = os.path.abspath(pkg_dirname)
    return pkg_paths
