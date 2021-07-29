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

## Usage

```python
from template_package.utils import iter_together
path_1 = "your file path 1"
path_2 = "your file path 2"
results = iter_together(path_1, path_2)
```
