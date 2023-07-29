from django.shortcuts import render, redirect
from .models import FibonacciNumber
from .calculate_fibonacci import calculate_fibonacci


def n_is_non_negative_number(value):
    # ensure input value is not negative
    try:
        n = int(value)
        return n >= 0
    except ValueError:
        return False


def fibonacci_input_view(request):
    error_message = None
    if request.method == "POST":
        n = request.POST.get("n")
        if n_is_non_negative_number(n):
            n = int(n)
            fibonacci_sequence = calculate_fibonacci(n)
            return redirect("fibonacci_output_view", pk=n)
        else:
            error_message = "Please enter a non-negative number."

    return render(request, "fibonacci_input.html", {"error_message": error_message})


def fibonacci_output_view(request, pk):
    fibonacci_entry_seq = FibonacciNumber.objects.filter(n=pk).first()
    fibonacci_sequence = fibonacci_entry_seq.fibonacci_sequence.split(",")
    # get previous page using HTTP_REFERER
    back_url = request.META.get("HTTP_REFERER", "/")
    return render(
        request,
        "fibonacci_output.html",
        {"fibonacci_sequence": fibonacci_sequence, "back_url": back_url},
    )
