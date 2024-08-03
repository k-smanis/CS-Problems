from typing import Dict


class InvalidFibonacciInput(Exception):
    def __init__(
        self, message="The integer number you enter must be greater or equal to 1."
    ):
        self.message = message
        super().__init__(self.message)


def find_fibonacci_number(n: int, memo: Dict[int, int] = {1: 1, 2: 2}):
    """This function calculates the N-th number of the fibonacci sequence, using a recursive approach.
    This implementation uses memoization to avoid duplicate computation of sub-trees."""
    if n < 1:
        raise InvalidFibonacciInput()

    if n in memo.keys():
        return memo[n]
    else:
        memo[n] = find_fibonacci_number(n - 1, memo) + find_fibonacci_number(
            n - 2, memo
        )

    return memo[n]


if __name__ == "__main__":

    print("This program calculates the N-th number of the fibonacci sequence.")
    EXAMPLE_N: int = 50

    try:
        fibonacci_number = find_fibonacci_number(n=EXAMPLE_N)
        print(f"The value of the #{EXAMPLE_N} fibonacci number is {fibonacci_number}.")
    except InvalidFibonacciInput as e:
        print(e.message)
