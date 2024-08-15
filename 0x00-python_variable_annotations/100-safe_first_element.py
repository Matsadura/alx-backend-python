#!/usr/bin/env python3
""" Contains the safe_first_element function"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Returns the first element"""
    if lst:
        return lst[0]
    else:
        return None
