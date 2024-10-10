#!/usr/bin/env python3
"""
a type annotation function safe_first_element
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a list or None if the list is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
