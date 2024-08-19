#!/usr/bin/env python3
""" Contains an asynchronous coroutine """
import asyncio
import random
from typing import Awaitable, Any


async def wait_random(max_delay: float = 10) -> float:
    """ Takes an argument, waits for a random relay
        and returns it eventually"""
    num = random.uniform(0, max_delay)
    return num
