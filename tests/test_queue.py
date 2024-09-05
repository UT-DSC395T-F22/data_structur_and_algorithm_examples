from my_collections.queue import Queue
import pytest

def test_queue() -> None:
    """
    Test the Queue class.
    """
    queue = Queue()
    assert len(queue) == 0
    assert queue.is_empty()

    queue.push(1)
    assert len(queue) == 1
    assert not queue.is_empty()
    queue.push(2)
    assert len(queue) == 2
    assert queue.pop() == 1
    assert len(queue) == 1
    assert not queue.is_empty()