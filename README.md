# pycd


[![PyPI Version](https://img.shields.io/pypi/v/pycd.svg)](https://pypi.python.org/pypi/pycd)
[![image](https://travis-ci.org/wkentaro/pycd.svg)](https://travis-ci.org/wkentaro/pycd)

Simple command line tool to change directory for Python packages.  
You can now easily read the codes of the modules.


## Installation

install pycd by pip

```bash
pip install pycd
```


add following line to your shell

```bash
source `which pycd.sh`
```

## Usage

use `pycd` to change directory for python packages:

```bash
$ pycd numpy
$ pwd
/usr/local/lib/python2.7/dist-packages/numpy
```

use `pypack` to get information about python packages:

```bash
$ pypack find numpy
/usr/local/lib/python2.7/dist-packages/numpy

$ pypack list
numpy
sklearn
scipy
...
```

## Testing

```bash
nosetests -v pycd
```


## License

See [LICENSE](LICENSE).
