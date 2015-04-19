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
  $ pycd_py install
  Please add below to your shell config file
  >   source /usr/local/lib/python2.7/dist-packages/pycd/pycd.sh
  add to /home/wkentaro/.zshrc? [y/N]: y
  $ cat ~/.zshrc

  # this line is added by pycd
  source /usr/local/lib/python2.7/dist-packages/pycd/pycd.sh

Usage
=====
.. code-block:: sh

  $ pycd
  Usage: pycd <module_name>
  $ pycd numpy
  $ pwd
  /usr/lib/python2.7/dist-packages/numpy
  # read the code!
