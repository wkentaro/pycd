========
``pycd``
========

.. image:: https://img.shields.io/pypi/v/pycd.svg
.. image:: https://travis-ci.org/wkentaro/pycd.svg
.. image:: https://coveralls.io/repos/wkentaro/pycd/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/wkentaro/pycd?branch=master


| Simple command line tool to change directory for Python packages.
| You can now easily read the codes of the modules.


Installation
============

install pycd by pip::

   $ pip install pycd

add following line to your shell::

    source `which pycd.sh`


Usage
=====

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


Testing
=======

.. code-block:: sh

    $ nosetests -v pycd


License
=======
| Copyright (C) 2015 Kentaro Wada
| Released under the MIT license
| http://opensource.org/licenses/mit-license.php
