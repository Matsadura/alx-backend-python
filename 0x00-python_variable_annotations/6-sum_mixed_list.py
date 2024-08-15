#!/usr/bin/env python3
""" Contains the function sum_mixed_list"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sums of n from a mixed list as float"""
    sum: float = 0
    for n in mxd_lst:
        sum += n
    return sum
