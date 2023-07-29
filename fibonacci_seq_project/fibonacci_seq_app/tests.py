from django.test import TestCase
from django.urls import reverse
from .models import FibonacciNumber
from .calculate_fibonacci import calculate_fibonacci


class FibonacciCalculationTestCase(TestCase):
    def test_fibonacci_calculation(self):
        # test a few fib calculations.
        self.assertEqual(calculate_fibonacci(0), "0")
        self.assertEqual(calculate_fibonacci(1), "0,1")
        self.assertEqual(calculate_fibonacci(2), "0,1,1")
        self.assertEqual(calculate_fibonacci(10), "0,1,1,2,3,5,8,13,21,34,55")


class FibonacciViewTestCase(TestCase):
    def test_fibonacci_input_view(self):
        # test input view renders
        response = self.client.get(reverse("fibonacci_input_view"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<label for="n">Enter a number (n):</label>')
        self.assertContains(
            response, '<input type="number" min=”0” name="n" id="n" required>'
        )

    def test_fibonacci_output_view(self):
        # test output view renders
        fibonacci_entry_seq = FibonacciNumber.objects.create(
            n=1, fibonacci_sequence="0,1"
        )
        print(
            f"Primary Key of created FibonacciNumber object: {fibonacci_entry_seq.pk}"
        )
        response = self.client.get(
            reverse("fibonacci_output_view", args=[fibonacci_entry_seq.pk])
        )
        self.assertEqual(response.status_code, 200)
