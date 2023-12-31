from django.db import models
from django.core.validators import MinValueValidator


class FibonacciNumber(models.Model):
    # ensure only pos ints with MinValueValidator
    n = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    fibonacci_sequence = models.TextField()

    def __str__(self):
        return f"Fib seq for n={self.n}"
