class ListNode:
    """A node of a singly linked list."""

    def __init__(self, value: int, next_node: "ListNode | None" = None) -> None:
        self.value = value
        self.next = next_node

    def __repr__(self) -> str:
        return f"ListNode({self.value})"


def reverse_list(head: ListNode | None) -> ListNode | None:
    """Reverse a singly linked list by changing the links between its nodes.

    Args:
        head: The first node of the list, or None if the list is empty.

    Returns:
        The first node of the reversed list, or None if the list is empty.
    """
    pass
