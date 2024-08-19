![image](https://github.com/user-attachments/assets/483ed0ef-687f-4363-b10f-6aa72dc06b95)

---

# Python Asynchronous Programming Guide

## Table of Contents

1. [Introduction](#introduction)
2. [Async and Await Syntax](#async-and-await-syntax)
   - [Understanding Coroutines](#understanding-coroutines)
   - [Basic Usage](#basic-usage)
3. [Executing an Async Program with asyncio](#executing-an-async-program-with-asyncio)
4. [Running Concurrent Coroutines](#running-concurrent-coroutines)
   - [Using asyncio.gather](#using-asynciogather)
   - [Using asyncio.wait](#using-asynciowait)
5. [Creating asyncio Tasks](#creating-asyncio-tasks)
6. [Using the random Module in an Async Context](#using-the-random-module-in-an-async-context)

## Introduction

Asynchronous programming in Python allows you to write programs that can perform tasks concurrently, making them more efficient, especially when dealing with I/O-bound operations. The `asyncio` library, introduced in Python 3.4, provides a foundation for writing asynchronous code using the `async` and `await` syntax.

## Async and Await Syntax

### Understanding Coroutines

Coroutines are the building blocks of asynchronous programming in Python. A coroutine is a special type of function that can pause and resume its execution. Coroutines are defined using the `async def` syntax and are used with the `await` keyword to perform asynchronous tasks.

### Basic Usage

Here's a basic example of a coroutine:

```python
import asyncio

async def greet(name: str) -> None:
    print(f"Hello, {name}!")
    await asyncio.sleep(1)
    print(f"Goodbye, {name}!")

# To run the coroutine, we need an event loop (explained later)
```

In this example, `greet` is a coroutine that prints a greeting, pauses for a second, and then prints a goodbye message. The `await` keyword is used to pause the coroutine until the `asyncio.sleep(1)` call is complete.

## Executing an Async Program with asyncio

To run an async program, you need to use an event loop, which is responsible for executing coroutines and managing their execution.

```python
async def main() -> None:
    await greet("Alice")

# Running the async program
if __name__ == "__main__":
    asyncio.run(main())
```

In this example, `asyncio.run(main())` starts the event loop and runs the `main` coroutine, which in turn calls the `greet` coroutine.

## Running Concurrent Coroutines

One of the key benefits of asynchronous programming is the ability to run coroutines concurrently. This means that multiple coroutines can be executed without blocking each other.

### Using asyncio.gather

`asyncio.gather` allows you to run multiple coroutines concurrently and wait for all of them to complete.

```python
async def greet_many() -> None:
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    )

asyncio.run(greet_many())
```

In this example, the `greet` coroutine is called concurrently for "Alice", "Bob", and "Charlie". All greetings are printed before the goodbyes, demonstrating that the coroutines are running concurrently.

### Using asyncio.wait

`asyncio.wait` is another method to run coroutines concurrently, but it provides more control over how the coroutines are handled.

```python
async def greet_many() -> None:
    tasks = [
        greet("Alice"),
        greet("Bob"),
        greet("Charlie")
    ]
    done, pending = await asyncio.wait(tasks)

asyncio.run(greet_many())
```

Here, `asyncio.wait` returns two sets: `done` for completed coroutines and `pending` for those that haven't finished yet.

## Creating asyncio Tasks

`asyncio.Task` is used to schedule the execution of a coroutine. Unlike `asyncio.gather`, which waits for all coroutines to complete, creating a task allows the coroutine to run in the background.

```python
async def main() -> None:
    task = asyncio.create_task(greet("Alice"))
    await task  # Wait for the task to complete

asyncio.run(main())
```

In this example, `asyncio.create_task` schedules the `greet` coroutine to run concurrently with the rest of the program. The `await task` line waits for the task to complete before moving on.

## Using the random Module in an Async Context

The `random` module is used to generate random numbers, but care should be taken when using it in an async context, as it can introduce blocking behavior if not used correctly.

### Generating a Random Number

```python
import random

async def random_sleep() -> None:
    sleep_time = random.uniform(0.5, 2.0)
    await asyncio.sleep(sleep_time)
    print(f"Slept for {sleep_time:.2f} seconds")

async def main() -> None:
    await asyncio.gather(
        random_sleep(),
        random_sleep(),
        random_sleep()
    )

asyncio.run(main())
```

In this example, `random.uniform(0.5, 2.0)` generates a random float between 0.5 and 2.0, which is then used to determine the sleep time of each coroutine. The coroutines run concurrently, and each will sleep for a random amount of time.

### Using Random Choices

```python
async def random_choice() -> None:
    choices = ["apple", "banana", "cherry"]
    choice = random.choice(choices)
    print(f"Random choice: {choice}")

async def main() -> None:
    await asyncio.gather(
        random_choice(),
        random_choice(),
        random_choice()
    )

asyncio.run(main())
```

In this example, `random.choice(choices)` selects a random item from the list of `choices`. Each coroutine picks a random fruit, and the results are printed.

---
