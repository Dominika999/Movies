from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render

def hello_world(request):
    our_context = {"time": datetime.now()}
    return render(request, 
                  template_name="hello.html",
                  context=our_context)
    return HttpResponse("Witaj świecie!")