from typing import Iterator




def red(text):
    return f"\033[31m{text}\033[0m"

def green(text):
    return f"\033[32m{text}\033[0m"

def yellow(text):
    return f"\033[33m{text}\033[0m"

def blue(text):
    return f"\033[34m{text}\033[0m"

def magenta(text):
    return f"\033[35m{text}\033[0m"

def cyan(text):
    return f"\033[36m{text}\033[0m"


colors = [red, green, yellow, blue, magenta, cyan]


def average(numbers: list[int]):
    return sum(numbers) / len(numbers)


def next_or_none(iterator: Iterator[any]) -> any:
    try:
        return next(iterator)
    except StopIteration:
        return None
