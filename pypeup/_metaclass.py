# -*- coding: utf-8 -*-
from ._utils import _return_self, _exec_context
import re

exclude_pattern = re.compile(r"__[A-Za-z]+__|register")
private_pattern = re.compile(r"_[A-Za-z0-9]+__[A-Za-z0-9]+|_[A-Za-z0-9]+_?")

class PipeMeta(type):

    def __new__(mcls, cname, bases, attributes):

        for method_name, method in attributes.items():
            if not exclude_pattern.match(method_name) and "__call__" in dir(method):
                attributes[method_name] = _exec_context(_return_self(method))

            if private_pattern.match(method_name) and "__call__" in dir(method):
                attributes[method_name] = _exec_context(method)

        return super(PipeMeta, mcls).__new__(mcls, cname, bases, attributes)
