from typing import Generator


# This generator yields "int" data, but receives nothing through "send", neither does it "return" anything
def fibonacci_number_generator() -> Generator[int, None, None]:
    """This function generates the next number of the fibonacci sequence."""

    previous: int = 0
    current: int = 1

    yield previous

    while True:
        previous, current = current, previous + current
        yield current


if __name__ == "__main__":

    print("This program generates the N first numbers of the fibonacci sequence.")
    EXAMPLE_N: int = 20

    fibonacci_number_generator_instance = fibonacci_number_generator()

    for _ in range(EXAMPLE_N):
        next_fibonacci: int = next(fibonacci_number_generator_instance)
        print(next_fibonacci)
