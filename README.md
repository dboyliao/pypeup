# pypeup - Piping Up with Python

[![Build Status](https://travis-ci.org/dboyliao/pypeup.svg?branch=master)](https://travis-ci.org/dboyliao/pypeup)

This is a simple python module to help you to build a data pipe in python.

## First Glance

Suppose you have a bunch of functions dealing with data of the same structure (e.g they are all `array`, `integer`, ...etc) and you want to pipe them up for complex computations, `pypeup` is here at your service.

With `pypeup`, you can write something like this:

```{python}
from pypeup import DataPipe

# Note that these two funtion all return the same data structure and their
# first arguments are all data.
# In this example, the data are all of type list.

def fun1(data, x):
    """
    x: <number>
    data: <list>
    """
    return [a + x for a in data]

def fun2(data, ind):
    """
    ind: <integer>
    data: <list>
    """
    return data[:min(ind, len(data) - 1)]

class MyPipe(DataPipe):
    pass

my_pipe = MyPipe([1, 2, 3, 4, 5])
my_pipe.register(fun1)      # Use register method to add any method you like 
my_pipe.register(fun2)      # for your data.

my_pipe.fun1(1).fun2(3).fun2(2).fun1(3) # Pipe the function up at your wish
my_pipe.data                # Access the data by the `data` attribute
# >>> [5, 6]
```

Also, you can build up the pipe by one class declairation:

```{python}
from pypeup import DataPipe
import numpy as np

class MyPipe2(DataPipe):

    def add(self, x):
        return self.data + x

    def sub(self, x):
        return self.data - x

    def mul(self, x):
        return self.data * x

pipe2 = MyPipe2(np.array([1, 2, 3]))
pipe2.add(3).sub(2).mul(4)
pipe2.data
# >>> np.array([8, 12, 16])
```

You can use private method as normal python:

```{python}
from pypeup import DataPipe
import math

class MyPipe(DataPipe):

    def fun(self, x):
        return self._magic(x)

    def _magic(self, x):
        print "Where the magic happens!"
        return self.data + math.sin(x)

pipe = MyPipe(0.)
print pipe.fun(math.pi / 2).data
# >>> Where the magic happens!
# >>> 1.
```

In order to protect the data inside the pipe, any modification to the `data` which is outside of the execution context of the methods of the pipe is not allowed and an `ExecutionContextError` will be raised.

```{python}
from pypeup import DataPipe

class MyPipe(DataPipe):

    def addOne(self):
        return self.data + 1

pipe = MyPipe(10)
pipe.addOne(1)     # OK.
pipe.data = 11     # Not OK.
```

There are some limits on the functions which can be applied to `pypeup`.
See [Limits](https://github.com/dboyliao/pypipe#limits) for detail.

## Limits

As mentioned above, there are few limits on the functions that can be used with `pypeup`:

- The current data can be access through `self.data`.
    - `self.data` is a `property` defined in `DataPipe`, which means that if you want to overwrite it, you must be sure your implementation is OK.
- All the functions' first argument must be `data`. (But not method, see below)
    - It doesn't mean you have to name it as `data`, but you have to be sure that all the functions' first argument will hold the data you want to process.
    - If the function is defined as an instance method, you only need to pass all the parameters needed to work with the data which can be access through `self.data`.
    - If the instance method is private method (method with the name start with `_` or `__`) will work just like normal instance method.
- All the `data` must be of the same (or compatible) data structure or type.
    - for example, they must be all `list`, `number`, `numpy.array`...etc.
- All the function must return the data which will be passed through the pipe.

## Installation

- Install through `pip`:
    - Just run `pip install pypeup`
- Install from source:
    - run `git clone https://github.com/dboyliao/pypeup.git && cd pypeup`
    - run `python setup.py install` to install the package.

## Tests

- If you haven't installed `nose` yet, run `pip install -r requirements.txt` first.
- run `nosetests`
