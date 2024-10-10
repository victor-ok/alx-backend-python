#!/usr/bin/env python3
"""
a type annotation function to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    converts
    Args:
        k(str): a given str
        v(Union): a union variable of an int and a float
    Returns:
        Tuple: tuple
    """
    return k, v ** 2
