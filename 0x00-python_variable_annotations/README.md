![image](https://github.com/user-attachments/assets/5980ca18-6b17-44d7-b859-fd75bf5026ca)

---

# Python Type Annotations and Type Checking

## Table of Contents

1. [Introduction](#introduction)
2. [Type Annotations in Python 3](#type-annotations-in-python-3)
   - [Basic Syntax](#basic-syntax)
   - [Using Type Annotations for Variables](#using-type-annotations-for-variables)
   - [Type Annotations in Function Signatures](#type-annotations-in-function-signatures)
3. [Duck Typing in Python](#duck-typing-in-python)
   - [What is Duck Typing?](#what-is-duck-typing)
   - [Duck Typing vs. Type Annotations](#duck-typing-vs-type-annotations)
4. [Validating Your Code with mypy](#validating-your-code-with-mypy)
   - [Installing mypy](#installing-mypy)
   - [Running mypy on Your Code](#running-mypy-on-your-code)
   - [Common mypy Options](#common-mypy-options)
   - [Handling mypy Errors](#handling-mypy-errors)

## Introduction

Type annotations in Python are a feature that allows you to specify the expected types of variables, function parameters, and return values. While Python is a dynamically typed language, type annotations provide a way to make your code more explicit, improving readability and enabling static type checking with tools like `mypy`.

## Type Annotations in Python 3

### Basic Syntax

Type annotations in Python are added using a colon `:` after a variable or parameter name, followed by the type. The `->` symbol is used to specify the return type of a function.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

In this example, `name` is annotated with the `str` type, and the function is expected to return a `str`.

### Using Type Annotations for Variables

You can also use type annotations for variables in your code. This is done by specifying the type after the variable name.

```python
age: int = 25
name: str = "Alice"
is_student: bool = True
```

While Python doesn't enforce these types at runtime, they serve as documentation and can be checked using static type checkers like `mypy`.

### Type Annotations in Function Signatures

Type annotations are particularly useful in function signatures, where they specify the types of arguments and return values.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Here, both `a` and `b` are expected to be integers, and the function returns an integer. If you pass arguments of incorrect types, tools like `mypy` can catch these mistakes before runtime.

#### Example with Optional and Union Types

Sometimes, a function parameter can be of multiple types or optional. The `Optional` and `Union` types from the `typing` module are useful in such cases.

```python
from typing import Optional, Union

def format_number(value: Union[int, float]) -> str:
    return f"{value:.2f}"

def greet(name: Optional[str] = None) -> str:
    return f"Hello, {name or 'Guest'}!"
```

## Duck Typing in Python

### What is Duck Typing?

Duck typing is a concept in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. The term comes from the phrase, "If it looks like a duck, swims like a duck, and quacks like a duck, then it probably is a duck."

For example:

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def animal_says(animal):
    return animal.speak()

dog = Dog()
cat = Cat()

print(animal_says(dog))  # Output: Woof!
print(animal_says(cat))  # Output: Meow!
```

Here, `animal_says` works with any object that has a `speak` method, regardless of the object's type.

### Duck Typing vs. Type Annotations

Duck typing focuses on the methods and properties an object has, rather than its type. Type annotations, on the other hand, specify explicit types and can be checked statically. While duck typing is flexible, type annotations provide more safety and clarity, especially in large codebases.

## Validating Your Code with mypy

### Installing mypy

To start using `mypy` for type checking, you first need to install it. You can install `mypy` using `pip`:

```bash
pip install mypy
```

### Running mypy on Your Code

Once installed, you can run `mypy` on your Python files to check for type errors.

```bash
mypy my_script.py
```

If `mypy` finds any type inconsistencies or errors, it will report them.

### Common mypy Options

- **Ignoring Errors**: You can ignore specific lines or files by using comments.
  ```python
  x = "Hello"  # type: ignore
  ```

- **Checking Unannotated Code**: By default, `mypy` only checks code with type annotations. You can instruct it to check untyped code too.
  ```bash
  mypy --check-untyped-defs my_script.py
  ```

- **Strict Mode**: Enable strict type checking.
  ```bash
  mypy --strict my_script.py
  ```

### Handling mypy Errors

`mypy` errors often point to mismatched types or missing type annotations. Fixing these errors involves ensuring that your code aligns with the expected types.

#### Example: Fixing a Type Error

Suppose `mypy` reports an error like this:

```bash
error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

This error occurs because a string was passed to a function expecting an integer. The solution is to pass the correct type:

```python
result = add(10, 20)  # Correct
result = add("10", "20")  # Incorrect, mypy will catch this
```

If you cannot fix a type issue, you can use the `# type: ignore` comment to suppress the error, though this should be done sparingly.

---
