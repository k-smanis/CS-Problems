class InvalidFibonacciInput(Exception):
    def __init__(
        self, message="The integer number you enter must be greater or equal to 1."
    ):
        self.message = message
        super().__init__(self.message)


def fib(N: int, memo={1: 1, 2: 2}):
    """This function calculates the N-th number of the fibonacci sequence"""
    if N < 1:
        raise InvalidFibonacciInput()

    if N in memo.keys():
        return memo[N]
    else:
        memo[N] = fib(N - 1, memo) + fib(N - 2, memo)

    return memo[N]


if __name__ == "__main__":

    print("This program calculates the N-th number of the fibonacci sequence.")
    EXAMPLE_N = 50

    try:
        fibonacci_number = fib(N=EXAMPLE_N)
        print(f"The value of the #{EXAMPLE_N} fibonacci number is {fibonacci_number}.")
    except InvalidFibonacciInput as e:
        print(e.message)
