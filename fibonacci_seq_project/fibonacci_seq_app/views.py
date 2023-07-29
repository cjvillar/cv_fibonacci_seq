from django.shortcuts import render, redirect
from .models import FibonacciNumber
from .calculate_fibonacci import calculate_fibonacci

def fibonacci_input_view(request):
    if request.method == "POST":
        n = int(request.POST.get("n"))
        #fibonacci_sequence = calculate_fibonacci(n)
        #return redirect("fibonacci_output", pk=n)
    return render(request, "fibonacci_input.html")


def fibonacci_output_view(request, pk):
    fibonacci_entry_seq = FibonacciNumber.objects.get(n=pk)
    fibonacci_sequence = fibonacci_entry_seq.fibonacci_sequence.split(',')
    return render(request, 'fibonacci_output.html', {'fibonacci_sequence': fibonacci_sequence})





