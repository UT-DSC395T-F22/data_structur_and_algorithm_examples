from my_collections.double_cirular_linked_list import DoubleCircularLinkedList, T
from typing import Iterator, Optional, Generic
class Stack(Generic[T]):

    def __init__(self) -> None:
        """
        Initializes a new instance of the Stack class.

        Args:
            None

        Returns:
            None
        """
        self._list: DoubleCircularLinkedList[T] = DoubleCircularLinkedList()
    
    def is_empty(self) -> bool:
        """
        Checks if the stack is empty.

        Args:
            None

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return self._list.is_empty()

    def push(self, data: T) -> None:
        """
        Pushes the given data onto the stack.

        Args:
            data (T): The data to be pushed onto the stack.

        Returns:
            None
        """
        self._list.append(data)

    def pop(self) -> Optional[T]:
        """
        Pops and returns the top element from the stack.

        Returns:
            Optional[T]: The top element in the stack, or None if the stack is empty.
        """
        return self._list.remove_last()

    def __len__(self) -> int:
        """
        Returns the number of elements in the stack.

        Args:
            None

        Returns:
            int: The number of elements in the stack.
        """
        return len(self._list)
    
    def __iter__(self) -> Iterator[T]:
        """
        Returns an iterator over the elements in the stack.

        Yields:
            Iterator[T]: The elements in the stack.
        """
        return self._list.__iter__()
    
    def __str__(self) -> str:
        """
        Returns a string representation of the stack.
        
        The string representation includes all elements in the stack, separated by ' -> '.
        If the stack is empty, it returns ''.
        
        Returns:
            str: A string representation of the stack.
        """
        if self._list.is_empty():
            return ""
        # Use __iter__ and join to convert to string
        return " -> ".join(map(str, self))
    
    def __repr__(self) -> str:
        """
        Returns a string representation of the stack.
        
        This method is used to provide a human-readable representation of the object.
        It returns the same string representation as the `__str__` method.
        """
        return self.__str__()

