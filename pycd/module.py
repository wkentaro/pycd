#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import imp
import pkgutil


def get_module_paths():
    module_paths = {}
    for module in pkgutil.iter_modules():
        module_name = module[1]
        try:
            file_, module_path = imp.find_module(module_name)[:2]
        except ImportError:
            continue
        module_dirname = os.path.split(module_path)[0]
        if file_ is None:
            module_paths[module_name] = os.path.abspath(module_path)
        else:
            module_paths[module_name] = os.path.abspath(module_dirname)
    return module_paths
