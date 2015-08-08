#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import os
import sys

from .cli import *
from .package import *
from .version import __version__


# get current PYTHONPATH
sys.path = os.getenv('PYTHONPATH').split(':') + sys.path
