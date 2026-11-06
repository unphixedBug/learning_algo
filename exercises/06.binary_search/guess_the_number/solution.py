def guess_number(n: int, check) -> int:
    """Find a secret number between 1 and n, using as few guesses as possible.

    Args:
        n: The biggest possible value of the secret. The smallest is 1.
        check: A function to call with a guess. It returns "higher" if the secret is
            bigger than the guess, "lower" if it is smaller, and "correct" if it is
            the secret.

    Returns:
        The secret number.
    """
    # Part 1: the numbers that are still possible, from low to high (both included).

    # Part 2: loop while at least one number is still possible.

        # Part 3: compute the middle of low and high, then call check() ONCE with it.

        # Part 4: handle the three possible answers.

    # Part 5: if the loop ends, something went wrong (see hint 2 in the README).
