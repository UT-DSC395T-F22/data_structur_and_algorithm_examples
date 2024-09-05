from typing import Optional, Generic, TypeVar, Iterator
from my_collections.comparable import Comparable

T = TypeVar("T", bound=Comparable)


class Node(Generic[T]):
    def __init__(
        self,
        data: T,
        prev_node: Optional["Node[T]"] = None,
        next_node: Optional["Node[T]"] = None,
    ) -> None:
        """
        Initializes a new instance of the Node class.

        Args:
            data (T): The data to be stored in the node.
            prev_node (Optional["Node[T]"]): The previous node in the linked list. Defaults to None.
            next_node (Optional["Node[T]"]): The next node in the linked list. Defaults to None.

        Returns:
            None
        """
        self._element: T = data
        self._prev_node: Optional["Node[T]"] = prev_node
        self._next_node: Optional["Node[T]"] = next_node

    def __str__(self) -> str:
        """
        Returns a string representation of the node, including its element and the elements of its next and previous nodes.
        """
        return f"{self._element=} {self._next_node._element=} {self._prev_node._element=}"

    def __repr__(self) -> str:
        """
        Returns a string representation of the object, which is the same as its string representation.
        
        Returns:
            str: A string representation of the object.
        """
        return self.__str__()


class DoubleCircularLinkedList(Generic[T]):
    def __init__(self) -> None:
        """
        Initializes a new instance of the DoubleCircularLinkedList class.

        Args:
            None

        Returns:
            None
        """
        self._head: Optional[Node] = None
        self._size: int = 0

    def _add_first(self, data: T) -> None:
        """
        Adds a new node with the given data to the beginning of the linked list.

        Args:
            data (T): The data to be stored in the new node.

        Returns:
            None
        """
        self._head = Node(data)
        self._head._next_node = self._head
        self._head._prev_node = self._head
        self._size += 1

    def append(self, data: T) -> None:
        """
        Appends the given data to the end of the double circular linked list.

        Args:
            data (T): The data to be appended to the list.

        Returns:
            None
        """
        if self._head is None:
            # Initialize the list with a single node that points to itself
            self._add_first(data)
        else:
            # Insert at the end of the list
            tail = self._head._prev_node
            _ = self._insert_between(data, tail, self._head)
    
    def prepend(self, data: T) -> None:
        """
        Prepends the given data to the beginning of the double circular linked list.

        Args:
            data (T): The data to be prepended to the list.

        Returns:
            None
        """
        if self._head is None:
            # Initialize the list with a single node that points to itself
            self._add_first(data)
        else:
            # Insert at the beginning of the list
            tail = self._head._prev_node
            new_node = self._insert_between(data, tail, self._head)
            self._head = new_node  # Update the head to the new node
    
    def remove_first(self) -> Optional[T]:
        """
        Removes and returns the first element from the double circular linked list.

        Returns:
            Optional[T]: The first element in the list, or None if the list is empty.
        """
        if self._head is None:
            return None
        element = self._delete_node(self._head)
        return element

    def remove_last(self) -> Optional[T]:
        """
        Removes and returns the last element from the double circular linked list.

        Returns:
            Optional[T]: The last element in the list, or None if the list is empty.
        """
        if self._head is None:
            return None
        element = self._delete_node(self._head._prev_node)
        return element

    def remove(self, data: T) -> Optional[T]:
        """
        Removes and returns the node with the given data from the double circular linked list.

        Args:
            data (T): The data to be removed from the list.

        Returns:
            Optional[T]: The removed element, or None if the data is not found in the list.
        """
        node: Optional[Node] = self.search(data)
        element: Optional[T] = None
        if node:
            element = self._delete_node(node)
        return element

    def search(self, data: T) -> Optional[Node]:
        """
        Searches for a node with the given data in the double circular linked list.

        Args:
            data (T): The data to be searched in the list.

        Returns:
            Optional[Node]: The node with the given data, or None if the data is not found in the list.
        """
        if self is None:
            return None
        current: Node = self._head
        found: Optional[Node] = None
        not_found = True
        while not_found:
            current = current._next_node
            if current._element == data:
                found = current
            if found or current == self._head:
                not_found = False
        return found

    def is_empty(self) -> bool:
        """
        Checks if the double circular linked list is empty.

        Args:
            None

        Returns:
            bool: True if the list is empty, False otherwise.
        """
        return self._size == 0

    def _insert_between(self, data: T, prev_node: Node, next_node: Node) -> Node:
        """
        Inserts a new node with the given data between two existing nodes in the double circular linked list.

        Args:
            data (T): The data to be stored in the new node.
            prev_node (Node): The previous node in the linked list.
            next_node (Node): The next node in the linked list.

        Returns:
            Node: The newly inserted node.
        """
        node = Node(data, prev_node, next_node)
        prev_node._next_node = node
        next_node._prev_node = node
        self._size += 1
        return node

    def _delete_node(self, node: Node) -> T:
        """
        Deletes a specified node from the double circular linked list and returns its element.

        Args:
            node (Node): The node to be deleted from the list.

        Returns:
            T: The element of the deleted node.
        """
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
        """
        Returns an iterator over the elements in the double circular linked list.

        Yields:
            T: The elements in the linked list.
        """
        if self._head is None:
            return
        current = self._head
        yield current._element
        current = current._next_node
        while current != self._head:
            yield current._element
            current = current._next_node

    def __len__(self) -> int:
        """
        Returns the number of elements in the double circular linked list.

        Args:
            None

        Returns:
            int: The number of elements in the list.
        """
        return self._size

    def __str__(self) -> str:
        """
        Returns a string representation of the double circular linked list.
        
        The string representation includes all elements in the list, separated by ' <-> '.
        If the list is empty, it returns ''.
        
        Returns:
            str: A string representation of the double circular linked list.
        """
        if self._head is None:
            return ""
        # Use __iter__ and join to convert to string
        return "<- " + " <-> ".join(map(str, self)) + " ->"

    def __repr__(self) -> str:
        """
        Returns a string representation of the double circular linked list.
        
        This method is used to provide a human-readable representation of the object.
        It returns the same string representation as the `__str__` method.
        
        Returns:
            str: A string representation of the double circular linked list.
        """
        return self.__str__()
