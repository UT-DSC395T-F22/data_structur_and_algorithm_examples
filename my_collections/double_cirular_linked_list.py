from typing import Optional, Generic, TypeVar, Iterator
from my_collections.comparable import Comparable

# have the
T = TypeVar("T", bound=Comparable)


class _Node(Generic[T]):
    def __init__(
        self,
        data: T,
        prev_node: Optional["_Node[T]"] = None,
        next_node: Optional["_Node[T]"] = None,
    ) -> None:
        self._element: T = data
        self._prev_node: Optional["_Node[T]"] = prev_node
        self._next_node: Optional["_Node[T]"] = next_node

    def __str__(self) -> str:
        return f"{self._element=} {self._next_node._element=} {self._prev_node._element=}"

    def __repr__(self) -> str:
        return self.__str__()


class DoubleCircularLinkedList(Generic[T]):
    def __init__(self) -> None:
        self._head: Optional[_Node] = None
        self._size: int = 0

    def _add_first(self, data: T) -> None:
        self._head = _Node(data)
        self._head._next_node = self._head
        self._head._prev_node = self._head
        self._size += 1

    def append(self, data: T) -> None:
        if self._head is None:
            # Initialize the list with a single node that points to itself
            self._add_first(data)
        else:
            # Insert at the end of the list
            tail = self._head._prev_node
            _ = self._insert_between(data, tail, self._head)
    
    def prepend(self, data: T) -> None:
        if self._head is None:
            # Initialize the list with a single node that points to itself
            self._add_first(data)
        else:
            # Insert at the beginning of the list
            tail = self._head._prev_node
            new_node = self._insert_between(data, tail, self._head)
            self._head = new_node  # Update the head to the new node

    def remove_last(self) -> Optional[T]:
        if self._head is None:
            return None
        element = self._delete_node(self._head._prev_node)
        return element

    def remove(self, data: T) -> Optional[T]:
        node: Optional[_Node] = self.search(data)
        element: Optional[T] = None
        if node:
            element = self._delete_node(node)
        return element

    def search(self, data: T) -> Optional[_Node]:
        if self is None:
            return None
        current: _Node = self._head
        found: Optional[_Node] = None
        not_found = True
        while not_found:
            current = current._next_node
            if current._element == data:
                found = current
            if found or current == self._head:
                not_found = False
        return found

    def is_empty(self) -> bool:
        return self._size == 0

    def _insert_between(self, data: T, prev_node: _Node, next_node: _Node) -> _Node:
        """Add element data between two existing nodes and return new node."""
        node = _Node(data, prev_node, next_node)
        prev_node._next_node = node
        next_node._prev_node = node
        self._size += 1
        return node

    def _delete_node(self, node: _Node) -> T:
        """Delete node from the list and return its element."""
        if self._size == 1:
            # Deleting the only node in the list
            element = node._element
            self._head = None
        else:
            prev_node = node._prev_node
            next_node = node._next_node
            prev_node._next_node = next_node
            next_node._prev_node = prev_node
            if node == self._head:
                self._head = next_node  # Update head if needed
            element = node._element
        self._size -= 1
        node._prev_node = node._next_node = node._element = None  # Deprecate node
        return element

    def __iter__(self) -> Iterator[T]:
        if self._head is None:
            return
        current = self._head
        while True:
            yield current._element
            current = current._next_node
            if current == self._head:
                break

    def __len__(self) -> int:
        return self._size

    def __str__(self) -> str:
        if self._head is None:
            return "<- Empty ->"
        # Use __iter__ and join to convert to string
        return "<-" + "<->".join(map(str, self)) + "->"

    def __repr__(self) -> str:
        return self.__str__()
