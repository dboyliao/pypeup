# -*- coding: utf-8 -*-

__all__ = ["DataPipe"]
__author__ = "DboyLiao <qmalliao@gmail.com>"
__license__ = "MIT"
__version__ = ("0", "5")

from ._metaclass import PipeMeta
from functools import wraps

class DataPipe(object):

    __metaclass__ = PipeMeta

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def register(self, fun):

        @wraps(fun)
        def wrapped(*args, **kwargs):
            
            new_data = fun(self.data, *args, **kwargs)
            self.data = new_data
            return self

        setattr(self, fun.__name__, wrapped)
