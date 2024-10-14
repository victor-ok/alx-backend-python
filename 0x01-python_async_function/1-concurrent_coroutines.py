#!/usr/bin/env python3
"""
Multiple coroutines with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax')


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    executing multiple coroutines at the same time with async
    Args:
        n: number of times to spawn wait_random
        max_delay: maximum delay between each call
    Returns:
        list of delays
    """
    tasks: List = [wait_random(max_delay) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]
