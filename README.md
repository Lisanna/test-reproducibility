# test-reproducibility

This package has some utilities for iterating over files.

## Installation

### Pip install from the repository

The code can be installed with:
```shell
$ pip install git+https://github.com/Lisanna/test-reproducibility
```

### Install in development mode

The code can be cloned in development mode with:
```shell
$ git clone https://github.com/Lisanna/test-reproducibility
```

Installing template package:
```shell
$ cd test-reproducibility 
$ pip install --editable .
```

Run tests:
```shell
$ pip install tox
$ tox
```

Init Sphinx documentation:
```shell
$ pip install sphinx
$ mkdir docs
$ cd docs
$ sphinx-quickstart

> Separate source and build directories (y/n) [n]: y
> Project name: Template Package
> Author name(s): Lisanna Paladin
> Project release []: 0.0.1-dev
> Project language [en]: 
```

Then change in `docs/conf.py`: 
```python
sys.path.insert(0, os.path.abspath('../../src'))
...
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode'
]
...
html_theme = 'sphinx_rtd_theme'
```

And run:
```shell
$ pip install sphinx-rtd-theme
$ cd docs
$ make html
```

In `docs/source/index.rst`:
```rst
.. toctree::
   :maxdepth: 2
   :caption: Contents:

   utils
```

Add `docs/source/utils.rst` file:
```rst
Utility Functions
=================

.. automodule:: template_package.utils
    :members:
```

## Usage

```python
from template_package.utils import iter_together
path_1 = "your file path 1"
path_2 = "your file path 2"
results = iter_together(path_1, path_2)
```
