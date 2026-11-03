import time

from solution import ListNode, reverse_list

# More than the longest list in these tests. Walking further means the links form a circle.
MAX_NODES = 300000


def build_list(values: list[int]) -> ListNode | None:
    """Build a linked list from a Python list, and return its first node."""
    head = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_nodes(head: ListNode | None) -> list[ListNode]:
    """Collect the nodes of a linked list, and fail clearly if the links form a circle."""
    nodes = []
    current = head
    while current is not None:
        nodes.append(current)
        assert len(nodes) <= MAX_NODES, "The links form a circle: the list never ends"
        current = current.next
    return nodes


def to_values(head: ListNode | None) -> list[int]:
    """Collect the values of a linked list, in order."""
    return [node.value for node in to_nodes(head)]


# --- Examples from the README ---


def test_several_nodes():
    assert to_values(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]


def test_two_nodes():
    assert to_values(reverse_list(build_list([1, 2]))) == [2, 1]


def test_one_node():
    assert to_values(reverse_list(build_list([7]))) == [7]


def test_empty_list():
    assert reverse_list(None) is None


def test_duplicate_values():
    assert to_values(reverse_list(build_list([1, 1, 2]))) == [2, 1, 1]


# --- Edge cases ---


def test_negative_values_and_zero():
    assert to_values(reverse_list(build_list([-1000, 0, 1000]))) == [1000, 0, -1000]


def test_all_values_identical():
    assert to_values(reverse_list(build_list([4, 4, 4]))) == [4, 4, 4]


def test_palindrome_values():
    assert to_values(reverse_list(build_list([1, 2, 1]))) == [1, 2, 1]


def test_returns_the_old_last_node():
    head = build_list([1, 2, 3])
    old_last = to_nodes(head)[-1]

    assert reverse_list(head) is old_last


def test_old_first_node_becomes_the_end():
    # Forgetting this link leaves 1 and 2 pointing at each other: a circle.
    head = build_list([1, 2])

    reverse_list(head)

    assert head.next is None


def test_single_node_is_returned_unchanged():
    head = build_list([7])

    assert reverse_list(head) is head
    assert head.next is None


def test_keeps_the_same_node_objects():
    # Fails if you create new nodes, or if you only swap the values.
    head = build_list([1, 2, 3, 4])
    original_nodes = to_nodes(head)

    result_nodes = to_nodes(reverse_list(head))

    assert len(result_nodes) == len(original_nodes)
    for result_node, original_node in zip(result_nodes, reversed(original_nodes)):
        assert result_node is original_node


def test_node_values_are_not_changed():
    head = build_list([1, 2, 3])
    original_nodes = to_nodes(head)

    reverse_list(head)

    assert [node.value for node in original_nodes] == [1, 2, 3]


def test_reversing_twice_gives_the_original_list():
    head = build_list([1, 2, 3, 4, 5])

    assert to_values(reverse_list(reverse_list(head))) == [1, 2, 3, 4, 5]


# --- Performance ---


def test_performance_long_list():
    # A recursive solution fails here, because the list is deeper than Python's call limit.
    values = [value % 2001 - 1000 for value in range(200000)]
    head = build_list(values)

    start = time.perf_counter()
    result = reverse_list(head)
    elapsed = time.perf_counter() - start

    assert to_values(result) == values[::-1]
    assert elapsed < 1


def test_performance_many_short_lists():
    lists = [build_list([1, 2, 3]) for _ in range(50000)]

    start = time.perf_counter()
    results = [reverse_list(head) for head in lists]
    elapsed = time.perf_counter() - start

    assert all(result.value == 3 for result in results)
    assert elapsed < 1
