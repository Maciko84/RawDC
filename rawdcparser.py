from texttoemoji import ConvertToEmoji
from typing import Callable
def parse(obj):
    message = []
    for item in obj:
        if _functions[item["type"]]:
            message.append(_functions[item["type"]](item["content"]))
    return ''.join(message)

_functions = dict[str, Callable[[list[str]], str]]()
def Node(name: str):
    def Decorator(func: Callable[[list[str]], str]) -> Callable[[list[str]], str]:
        _functions[name] = func
        return func
    return Decorator
from nodes import *