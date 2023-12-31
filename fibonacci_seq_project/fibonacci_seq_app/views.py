"""

Improvments:
- removed request.META.get("HTTP_REFERER", "/") from back button 
and now use request.session.get("previous_url", "/")

"""

from django.shortcuts import render, redirect
from .models import FibonacciNumber
from .calculate_fibonacci import calculate_fibonacci


def fibonacci_input_view(request):
    if request.method == "POST":
        n = int(request.POST.get("n"))
        calculate_fibonacci(n)
        return redirect("fibonacci_output_view", pk=n)
    return render(request, "fibonacci_input.html")


def fibonacci_output_view(request, pk):
    fibonacci_entry_seq = FibonacciNumber.objects.filter(n=pk).first()
    fibonacci_sequence = fibonacci_entry_seq.fibonacci_sequence.split(",")
    
    # get previous URL 
    back_url = request.session.get("previous_url", "/")

    return render(
        request,
        "fibonacci_output.html",
        {"fibonacci_sequence": fibonacci_sequence, "back_url": back_url},
    )
