#!/usr/bin/env python3
"""
a type annotation function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    sums a list of float numbers
    Args:
        input_list(list): A list of floats
    Returns:
        float: The sum of the floats in the list
    """
    if input_list:
        return sum(input_list)
    else:
        return 0.0
