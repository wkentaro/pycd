====
pycd
====

**pycd** is simple command line tool to change directory for Python packages.  You can now easily read the codes of the modules.

The code is open source, and `available on github`_.

.. _available on github: http://github.com/wkentaro/pycd


.. toctree::
   :maxdepth: 1

   installation
   testing
   license


use ``pycd`` to change directory for python packages::

   $ pycd numpy
   $ pwd
   /usr/local/lib/python2.7/dist-packages/numpy


use ``pypack`` to get information about python packages::

   $ pypack find numpy
   /usr/local/lib/python2.7/dist-packages/numpy

   $ pypack list
   numpy
   sklearn
   scipy
   ...
