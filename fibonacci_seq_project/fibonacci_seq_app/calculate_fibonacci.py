"""
calculate_fibonacci calculates the fibonacci seq for all the terms up to the given nth term and saves n and fibonacci_sequence in a db.
If the nth terms fibonacci_sequence is in the database it will retreive to avoid redundant calculations.

If the databse is empty, calculate_fibonacci will initialize it with the base case data.
"""

from .models import FibonacciNumber


def set_base_case():
    if not FibonacciNumber.objects.exists():
        # set the base case if databse empty
        FibonacciNumber.objects.create(n=0, fibonacci_sequence="0")
        FibonacciNumber.objects.create(n=1, fibonacci_sequence="0,1")
        return True
    return False


def calculate_fibonacci(n):
    # check if base case set
    if set_base_case():
        pass

    # check if fib seq for n exists in db
    fibonacci_entry_seq = FibonacciNumber.objects.filter(n=n).first()

    if fibonacci_entry_seq:
        return fibonacci_entry_seq.fibonacci_sequence

    # get latest seq from db to build the next seq.
    last_seq = FibonacciNumber.objects.latest("n")
    fibonacci_sequence = list(map(int, last_seq.fibonacci_sequence.split(",")))
    num_0, num_1 = fibonacci_sequence[-2:]

    # calculate nth sequence iteratively from the last two numbers in the last sequence
    for i in range(len(fibonacci_sequence), n + 1):
        next_num = num_0 + num_1
        fibonacci_sequence.append(next_num)
        num_0, num_1 = num_1, next_num

        # store fib seq for n=i in db
        fibonacci_sequence_str = ",".join(map(str, fibonacci_sequence))
        FibonacciNumber.objects.create(n=i, fibonacci_sequence=fibonacci_sequence_str)

    return fibonacci_sequence_str
