#!/usr/bin/env python3
"""
a type annotation function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Multiplies a float by multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """
        multiplies a float by a multiplier
        Args:
            number: a float number
        Returns:
            Float
        """
        return multiplier * number
    return multiplier_func
