# -*- coding: utf-8 -*-

__all__ = ["ExecutionContextError"]

class ExecutionContextError(Exception): 
    """
    This exception will be raise if the data are going to modified
    outside of the execution of registed method.

    That is, something like this is not allowed:
        pipe = MyPipe(data)
        pipe.data = new_data  # Not allowed.
    """

    pass