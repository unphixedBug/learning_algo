def final_score(operations: list[str]) -> int:
    """Replay a list of scoring operations and return the total score.

    Args:
        operations: The operations to apply in order. Each one is "+", "D",
            "C", or a string representing an integer.

    Returns:
        The sum of every score left in the record once all operations
        have been applied.
    """
    record = []

    for op in operations:
        if not record and (op == "C" or op == "D") or len(record) < 2 and op == "+":
            raise ValueError

        if op == "+":
            record.append(record[-1] + record[-2])
        elif op == "D":
            record.append(record[-1] * 2)
        elif op == "C":
            record.pop()
        else:
            record.append(int(op))

    return sum(record)