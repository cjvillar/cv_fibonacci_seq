from django.urls import path
from . import views

urlpatterns = [
    path('', views.fibonacci_input_view, name='fibonacci_input_view'),
    path('<int:pk>', views.fibonacci_output_view, name='fibonacci_output_view'),
]