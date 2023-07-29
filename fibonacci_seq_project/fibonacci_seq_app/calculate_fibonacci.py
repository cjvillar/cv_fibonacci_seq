"""
calculate_fibonacci calculates the fibonacci seq for all the terms up to the given nth term and saves n and fibonacci_sequence in a db.
If the nth terms fibonacci_sequence is in the database it will retreive to avoid redundant calculations.

"""

from .models import FibonacciNumber


def calculate_fibonacci(n):
    # check if fib seq for n exists in db
    fibonacci_entry_seq = FibonacciNumber.objects.filter(n=n).first()

    if fibonacci_entry_seq:
        return fibonacci_entry_seq.fibonacci_sequence

    # if fib seq for n does not exist, calc
    fibonacci_sequence = []

    if n == 0:
        fibonacci_sequence = [
            0
        ]  # as per, https://www.mathsisfun.com/numbers/fibonacci-sequence.html
    elif n == 1:
        fibonacci_sequence = [0, 1]
    else:
        # calc fib seq using the existing seq for smaller n if exists
        # **the code below was refined and debugged using ChatGPT**
        previous_sequence_str = calculate_fibonacci(n - 1)
        previous_sequence = list(map(int, previous_sequence_str.split(",")))
        next_num = previous_sequence[-1] + previous_sequence[-2]
        # cat two list
        fibonacci_sequence = previous_sequence + [next_num]

    # store fib seq for n in db
    fibonacci_sequence_str = ",".join(map(str, fibonacci_sequence))
    FibonacciNumber.objects.get_or_create(
        n=n, defaults={"fibonacci_sequence": fibonacci_sequence_str}
    )

    return fibonacci_sequence_str
