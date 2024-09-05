from my_collections.double_cirular_linked_list import DoubleCircularLinkedList
import pytest


def test_double_cirular_linked_list():
    dll = DoubleCircularLinkedList()
    assert dll.is_empty()
    assert len(dll) == 0
    assert str(dll) == ""
    assert repr(dll) == ""

    dll.append(1)
    assert not dll.is_empty()
    assert len(dll) == 1
    assert str(dll) == "<- 1 ->"
    assert repr(dll) == "<- 1 ->"

    dll.prepend(2)
    assert len(dll) == 2
    assert str(dll) == "<- 2 <-> 1 ->"
    head_node = dll.search(2)
    assert head_node._element == 2
    assert head_node._next_node._element == 1
    assert head_node._prev_node._element == 1
    next_node = dll.search(1)
    assert next_node._element == 1
    assert next_node._next_node._element == 2
    assert next_node._prev_node._element == 2
    assert dll.search(3) is None
    assert dll.remove_last() == 1
    assert dll.remove_last() == 2
    assert dll.remove_last() is None
    assert dll.is_empty()