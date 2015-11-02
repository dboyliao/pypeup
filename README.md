# Piping in Python

This is a simple python module to help you to build a data pipe in python.

## First Glance

Suppose you have a bunch of functions dealing with data of the same structure (e.g they are all `array`, `integer`, ...etc) and you want to pipe them up for complex computations, `pypipe` is here at your service.

With `pypipe`, you can write something like this:

```{python}
from pypipe import DataPipe

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
my_pipe.data
# >>> [5, 6]
```

Also, you can build up the pipe by one class declairation:

```{python}
from pypipe import DataPipe
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

There are some limits on the functions which can be applied to `pypipe`.
See [Limits](https://github.com/dboyliao/pypipe#limits) for detail.

## Limits

As mentioned above, there are few limits on the functions that can be used with `pypipe`:

- All the functions' first argument must be `data`.
    - It doesn't mean you have to name it as `data`, but you have to be sure that all the functions' first argument will hold the data you want to process.
- All the `data` must be of the same (or compatible) data structure or type.
    - for example, they must be all `list`, `number`, `numpy.array`...etc.
- All the function must return the data which will be passed through the pipe.

## Installation

- run `git clone https://github.com/dboyliao/pypipe.git && cd pypipe`
- run `python setup.py install` to install the package.

## Tests

- If you haven't installed `nose` yet, run `pip install -r requirements.txt` first.
- run `nosetests`