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

add following line to user ``.zshrc``::

    antigen bundle wkentaro/pycd

for others
----------
install pycd by pip::

   $ pip install pycd

and download pycd from github::

    $ git clone https://github.com/wkentaro/pycd.git ~/.pycd

add following to your `.bashrc` or `.zshrc`::

    source ~/.pycd/pycd.sh
    source ~/.pycd/pycd-completion.bash


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
   $ pypkg find numpy
   /usr/local/lib/python2.7/dist-packages/numpy
   $ pypkg list
   numpy
   sklearn
   scipy
   ...


License
=======
| Copyright (C) 2015 Kentaro Wada
| Released under the MIT license
| https://github.com/wkentaro/pycd/blob/master/LICENSE
