from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request -> response
# request handler
# action


def say_hello(request): 
    # For example: pull data from db -> transform -> send email...
    # return HttpResponse('Hello World')
    return render(request, 'hello.html', {'name': 'Anne'})
