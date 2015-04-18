====
pycd
====
| Simple command line tool to change directory for Python packages.
| You can now easily read the codes of the modules.

Installation
============
pycd officially supports bash and zsh.

.. code-block:: sh

  git clone https://github.com/wkentaro/pycd.git ~/.pycd
  echo "source ~/.pycd/pycd.sh >> .bashrc"

Usage
=====
.. code-block:: sh

  $ pycd
  usage: pycd DIST_NAME
  $ pycd numpy
  $ pwd
  /usr/lib/python2.7/dist-packages/numpy
  # read the code!
