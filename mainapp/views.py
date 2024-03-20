from django.shortcuts import render, HttpResponse
from .tasks import test_func


# Create your views here.
def test(request):
    test_func.delay()  # this will run the task in the background and we continue with the rest of the code
    return HttpResponse("You just, waited")
