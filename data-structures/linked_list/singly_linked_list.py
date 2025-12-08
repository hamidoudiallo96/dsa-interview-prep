from list_node import ListNode
from typing import Any, Optional, cast


class SinglyLinkedList:
    def __init__(self) -> None:
        self.head: Optional[ListNode] = None
        self.tail: Optional[ListNode] = None
        self.size: int = 0

    def __str__(self):
        curr = self.head
        nodes = []

        while curr:
            nodes.append(str(curr.val))
            curr = curr.next

        return " => ".join(nodes)

    def __repr__(self):
        return f"SinglyLinkedList([{', '.join(map(str, self))}])"

    def __len__(self) -> int:
        return self.size

    def __contains__(self, item):
        return self.search(item)

    def insert_at_head(self, data: Any) -> None:
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:  # was empty
            self.tail = new_node
        self.size += 1

    def insert_at_tail(self, data: Any) -> None:
        if not self.tail:
            self.insert_at_head(data)
            return

        new_node = ListNode(data)
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def insert_at_pos(self, pos: int, data: Any) -> None:
        if pos < 0 or pos > self.size:
            raise IndexError("Index out of bounds")

        if pos == 0:
            self.insert_at_head(data)
            return

        if pos == self.size:
            self.insert_at_tail(data)
            return

        prev = cast(ListNode, self.head)

        for _ in range(pos - 1):
            prev = prev.next

        if prev.next is None:
            self.insert_at_tail(data)
            return

        new_node = ListNode(data)
        new_node.next = prev.next
        prev.next = new_node
        self.size += 1

    def insert_after_node(self, prev: Any, data: Any) -> None:
        if not self.head:
            self.insert_at_head(data)
            return

        curr = self.head
        new_node = ListNode(data)

        while curr and curr.val != prev:
            curr = curr.next

        if curr is None:
            raise ValueError("Value not found")

        next_node = curr.next
        curr.next = new_node
        new_node.next = next_node
        self.size += 1

    def delete_at_head(self) -> Any:
        if not self.head:
            raise ValueError("Empty List")

        node = self.head.val
        self.head = self.head.next
        self.size -= 1

        if self.head is None:  # one node
            self.tail = None
        return node

    def delete_after_node(self, prev: Any) -> Any:
        if not self.head:
            raise ValueError("Empty List")

        curr = self.head

        while curr and curr.val != prev:
            curr = curr.next

        if curr is None or curr.next is None:
            raise ValueError("No node to delete after given value")

        node = curr.next
        curr.next = node.next

        if curr.next is None:
            self.tail = curr

        self.size -= 1
        return node.val

    def delete_at_pos(self, pos: int) -> Any:
        if pos < 0 or pos >= self.size:
            raise IndexError("Index out of bounds")
        if pos == 0:
            return self.delete_at_head()
        if pos == self.size - 1:
            return self.delete_at_tail()

        curr = self.head

        for _ in range(pos - 1):
            curr = curr.next

        if curr.next is None:
            self.tail = curr

        node = curr.next
        curr.next = node.next
        self.size -= 1
        return node.val

    def delete_at_tail(self) -> Any:
        if not self.tail:
            raise ValueError("Empty List")

        # Special-case 1-element list
        if self.head is self.tail:  # single element
            node = self.head
            self.head = self.tail = None
            self.size = 0
            return node.val

        curr = cast(ListNode, self.head)
        while curr.next is not self.tail:
            curr = curr.next  # type: ignore[assignment]

        node = self.tail.val
        curr.next = None
        self.tail = curr
        self.size -= 1
        return node

    def search(self, data: Any) -> bool:
        if not self.head:
            raise ValueError("Empty List")

        curr = self.head

        while curr:
            if curr.val == data:
                return True
            curr = curr.next

        return False

    def node_at_pos(self, pos: int) -> ListNode:
        if pos < 0 or pos > self.size:
            raise IndexError("Index out of bounds")
        curr = cast(ListNode, self.head)

        for _ in range(pos):
            curr = curr.next
        return curr.val

    def reverse_list(self) -> None:
        if not self.head:
            raise ValueError("Empty List")

        curr = self.head
        prev = None
        self.tail = self.head  # update tail -> old head becomes new tail

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        self.head = prev


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_head(88)
    sll.insert_at_head(34)
    sll.insert_at_head(23)
    sll.insert_at_head(6)
    sll.insert_at_head(44)

    print(len(sll))  # 5
    print(sll)
    sll.insert_after_node(34, 97)
    sll.insert_at_pos(2, 98)
    sll.insert_at_tail(29)
    print(sll)  # 44 => 6 => 98 => 23 => 34 => 97 => 88 => 29

    print(sll.delete_at_head())  # 44
    print(sll.delete_at_tail())  # 29
    print(sll.delete_after_node(23))  # 34
    print(sll.delete_at_pos(2))  # 23
    print(sll)  # 6 => 98 => 97 => 88
    sll.reverse_list()
    print(sll)  # 88 => 97 => 98 => 6
    print(sll.node_at_pos(2))  # 98
