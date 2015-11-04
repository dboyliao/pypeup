# -*- coding: utf-8 -*-
__all__ = ['_return_self', '_exec_context']

from functools import wraps

def _return_self(method):

    @wraps(method)
    def wrapped(self, *funargs, **funkwargs):
        
        new_data = method(self, *funargs, **funkwargs)

        if not isinstance(new_data, type(self.data)):
            raise TypeError('All method should return velue of type {}: {} is returned.'.format(type(self.data), type(new_data)))

        self.data = new_data
        return self

    return wrapped

def _exec_context(method):

    @wraps(method)
    def wrapped(self, *funargs, **funkwargs):

        self._under_execution_context = True
        
        return method(self, *funargs, **funkwargs)

    return wrapped

        