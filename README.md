# Piping in Python

This is a simple python module to help you to build a data pipe in python.

## First Glance

Suppose you have a bunch of functions written before dealing with data with same structure (e.g they are all `array`, `integer`, ...etc) and you want to pipe them up for complex computations, `pypipe` is at your service.

With `pypipe`, you can write something like this:

```{python}
from pypipe import DataPipe

# Note that these two funtion all return the same data structure and their
# first argument are all data.
# These are the only requirements for using pypipe.
# In this example, the data are all of type list.

def fun1(data, x):
    """
    x: <number>
    data: <list>
    """
    return [a + x for a in data]

def fun2(data, ind)
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

my_pipe.fun1(1).fun2(2).fun2(1).fun1(3) # Pipe the function up at your wish
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
        reuturn self.data - x

    def mul(self, x):
        return self.data * x

pipe2 = MyPipe2(np.array([1, 2, 3]))
pipe2.add(3).sub(2).mul(4)
pipe2.data
# >>> np.array([8, 12, 16])

```

## Installation

- run `git clone https://github.com/dboyliao/pypipe.git && cd pypipe`
- run `python setup.py install` to install the package.

## Tests

- If you haven't installed `nose` yet, run `pip install -r requirements.txt` first.
- run `nosetests`
