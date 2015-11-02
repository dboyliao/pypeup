# -*- coding: utf-8 -*-
from ._utils import _return_self
import re

exclude_pattern = re.compile(r"__[A-Za-z]+__|register")

class PipeMeta(type):

    def __new__(mcls, name, bases, attributes):

        cls = super(PipeMeta, mcls).__new__(mcls, name, bases, attributes)

        for name, method in attributes.items():
            if not exclude_pattern.match(name) and "__call__" in dir(method):
                attributes[name] = _return_self(method)

        return super(PipeMeta, mcls).__new__(mcls, name, bases, attributes)