#!/usr/bin/env python3
""" Contains the function sum_list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of floats from a list of floats"""
    result: float = 0
    for n in input_list:
        result += n
    return result
