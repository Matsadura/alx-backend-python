#!/usr/bin/env python3
""" Contains make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function that multiplies a float
        by multiplier"""
    def multiFunction(multiplier: float) -> float:
        """Return the multiplication of n by multiplier"""
        return multiplier * 2.22
    return multiFunction
