#!/usr/bin/env python3
"""
Async function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random delay between 0 and max_delay
    """
    wait_time: float = random.uniform(0.0, float(max_delay))
    await asyncio.sleep(wait_time)
    return wait_time
