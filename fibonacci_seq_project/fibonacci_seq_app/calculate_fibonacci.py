"""
calculate_fibonacci calculates the fibonacci seq for all the terms up to the given nth term and saves n and fibonacci_sequence in a db.
If the nth terms fibonacci_sequence is in the database it will retreive to avoid redundant calculations.

If the databse is empty, calculate_fibonacci will initialize it with the base case data.


Imporvments: 
- split up calculate_fibonacci_sequence big function into multimple focused functions.
- added database transactions and a try catch error handler to rollback. 

"""

from .models import FibonacciNumber
from django.db import transaction, DatabaseError


def set_base_case():
    if not FibonacciNumber.objects.exists():
        # set the base case if databse empty
        FibonacciNumber.objects.create(n=0, fibonacci_sequence="0")
        FibonacciNumber.objects.create(n=1, fibonacci_sequence="0,1")
        return True
    return False


def get_existing_fibonacci(n):
    # check if fib seq for n exists in the database
    fibonacci_entry_seq = FibonacciNumber.objects.filter(n=n).first()
    return fibonacci_entry_seq.fibonacci_sequence if fibonacci_entry_seq else None


def calculate_fibonacci_sequence(n):
    # get the latest sequence from the database to build the next sequence
    last_seq = FibonacciNumber.objects.latest("n")
    fibonacci_sequence = list(map(int, last_seq.fibonacci_sequence.split(",")))
    num_0, num_1 = fibonacci_sequence[-2:]

    # cal nth sequence iteratively from the last two numbers in the last sequence
    for i in range(len(fibonacci_sequence), n + 1):
        next_num = num_0 + num_1
        fibonacci_sequence.append(next_num)
        num_0, num_1 = num_1, next_num

    return fibonacci_sequence


def save_fibonacci_sequence(n, fibonacci_sequence):
    # store the Fibonacci sequence for n in the database
    fibonacci_sequence_str = ",".join(map(str, fibonacci_sequence))
    try:
        with transaction.atomic():
            FibonacciNumber.objects.create(
                n=n, fibonacci_sequence=fibonacci_sequence_str
            )
    except DatabaseError as e:
        transaction.set_rollback(True)


def calculate_fibonacci(n):
    # check if base case set
    set_base_case()

    # Check if the Fibonacci sequence for n exists in the database
    existing_sequence = get_existing_fibonacci(n)
    if existing_sequence:
        return existing_sequence

    # calculate the Fibonacci sequence
    fibonacci_sequence = calculate_fibonacci_sequence(n)

    # save the Fibonacci sequence in the database
    save_fibonacci_sequence(n, fibonacci_sequence)

    return ",".join(map(str, fibonacci_sequence))
