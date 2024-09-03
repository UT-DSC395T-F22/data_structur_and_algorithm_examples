from my_collections.double_cirular_linked_list import DoubleCircularLinkedList


def main() -> None:
    dll = DoubleCircularLinkedList()
    dll.append(1)
    dll.append(2)
    dll.append(3)
    dll.prepend(0)
    print(dll)
    print(dll._size)
    print(dll.search(0))
    dll.remove_last()
    for i in dll:
        print(i)
    
    print(dll)


if __name__ == "__main__":
    main()
