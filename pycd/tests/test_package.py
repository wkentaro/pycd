#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from nose.tools import assert_true, assert_equal

from pycd.package import get_package_paths


def test_get_package_paths():
    package_paths = get_package_paths()
    assert_true(isinstance(package_paths, dict))
    this_dir = os.path.dirname(os.path.abspath(__file__))
    pycd_path = os.path.realpath(os.path.join(this_dir, '..'))
    assert_equal(package_paths['pycd'], pycd_path)
