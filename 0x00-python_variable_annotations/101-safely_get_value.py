#!/usr/bin/env python3
""" Contains safely_get_value function """
from typing import Union, Any, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """ Returns a value"""
    if key in dct:
        return dct[key]
    else:
        return default
