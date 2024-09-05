from my_collections.stack import Stack
import pytest

def test_stack():
    stack = Stack()
    stack.push("a")
    stack.push("B")
    stack.push(1)
    assert stack.pop() == 1
    assert stack.pop() == "B"
    assert stack.pop() == "a"
    assert stack.pop() is None