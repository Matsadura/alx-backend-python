#!/usr/bin/env python3
""" Contains an asynchronous coroutine """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Takes an argument, waits for a random relay
        and returns it eventually"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
