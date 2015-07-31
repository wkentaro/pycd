====
pycd
====
| Simple command line tool to change directory for Python packages.
| You can now easily read the codes of the modules.


Installation
============


for homebrew users
------------------
homebrew tap is available `wkentaro/homebrew-pycd <https://github.com/wkentaro/homebrew-pycd>`_.


for antigen users
-----------------
install pycd by pip::

   $ pip install pycd

add following line to your ``.zshrc``::

    antigen bundle wkentaro/pycd


for others
----------
install pycd by pip::

   $ pip install pycd

add following line to your shell::

    source `which pycd.sh`


Usage
=====
.. code-block:: sh

   $ pycd
   Usage: pycd <module_name>
   $ pycd numpy
   $ pwd
   /usr/local/lib/python2.7/dist-packages/numpy
   # read the code!

   # handling python package utils
   $ pypack find numpy
   /usr/local/lib/python2.7/dist-packages/numpy
   $ pypack list
   numpy
   sklearn
   scipy
   ...


License
=======
| Copyright (C) 2015 Kentaro Wada
| Released under the MIT license
| https://github.com/wkentaro/pycd/blob/master/LICENSE
