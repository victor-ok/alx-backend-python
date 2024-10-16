#!/usr/bin/env python3
"""
Async comprehensions with Python
"""
from typing import List


async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehensions"""
    numbers_list = [i async for i in async_generator()]
    return numbers_list
