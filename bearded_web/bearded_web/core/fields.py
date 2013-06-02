# -*- coding: utf-8 -*-

import inspect


class Choice(object):

    class __metaclass__(type):

        def __init__(cls, *args, **kwargs):
            cls._data = []
            for name, value in inspect.getmembers(cls):
                if not name.startswith("_") and not inspect.isfunction(value):
                    if isinstance(value, tuple) and len(value) > 1:
                        data = value
                    else:
                        data = (value, " ".join([x.capitalize() for x in name.split("_")]),)
                    cls._data.append(data)
                    cls._data = sorted(cls._data, key=lambda i: i[0])
                    setattr(cls, name, data[0])

        def __iter__(self):
            for value, data in self._data:
                yield value, data