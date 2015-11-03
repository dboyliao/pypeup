# -*- coding: utf-8 -*-
from ._utils import _return_self
import re

exclude_pattern = re.compile(r"__[A-Za-z]+__|register")

class PipeMeta(type):

    def __new__(mcls, cname, bases, attributes):

        for method_name, method in attributes.items():
            if not exclude_pattern.match(method_name) and "__call__" in dir(method):
                attributes[method_name] = _return_self(method)

        return super(PipeMeta, mcls).__new__(mcls, cname, bases, attributes)