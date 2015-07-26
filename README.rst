====
pycd
====
| Simple command line tool to change directory for Python packages.
| You can now easily read the codes of the modules.


Installation
============
pycd officially supports bash and zsh.

.. code-block:: sh

   $ pip install pycd


For Antigen users
-----------------
Add following line to user ``.zshrc``::

    antigen bundle wkentaro/pycd


For others
----------
download pycd from github::

    $ git clone https://github.com/wkentaro/pycd.git ~/.pycd

add following to your `.bashrc` or `.zshrc`::

    source ~/.pycd/pycd.sh
    source ~/.pycd/pycd-completion.bash  # also supports zsh


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
