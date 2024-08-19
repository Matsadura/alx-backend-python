#!/usr/bin/env python3
""" Contains the task_wait_random function """
import asyncio
from typing import Awaitable, Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Awaitable:
    """ Returns a asyncio.task """
    return asyncio.Task(wait_random(max_delay))
