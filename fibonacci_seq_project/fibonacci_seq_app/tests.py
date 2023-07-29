from django.test import TestCase
from django.urls import reverse
from .models import FibonacciNumber

class FibonacciViewTestCase(TestCase):
    def test_fibonacci_input_view(self):
        response = self.client.get(reverse('fibonacci_input_view'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<label for="n">Enter a number (n):</label>')
        self.assertContains(response, '<input type="number" min=”0” name="n" id="n" required>')
   
    def test_fibonacci_output_view(self):
         fibonacci_entry_seq = FibonacciNumber.objects.create(n=1, fibonacci_sequence='0,1')
         print(f"Primary Key of created FibonacciNumber object: {fibonacci_entry_seq.pk}")
         response = self.client.get(reverse('fibonacci_output_view', args=[fibonacci_entry_seq.n]))
         self.assertEqual(response.status_code, 200)


