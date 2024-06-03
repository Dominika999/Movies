from datetime import datetime 
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def hello_world(request):
    our_context = {"time": datetime.now()} 
    return render(
        request, 
        template_name="hello.html", 
        context=our_context
    ) 

from movies.models import Movie

def list_movies(request):
    movies = Movie.objects.all()
    return render(
        request,
        template_name="movie_list.html",
        context={"movies": movies}
    )

def user_profile(request):
    return render(
        request,
        template_name="registration/profile.html",
        context={"user": request.user}
    )

def user_signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request,
                template_name="registration/signup_complete.html",
        )
    else:
        form = UserCreationForm()
    return render(
        request,
        template_name="registration/signup_form.html",
        context={"form": form},
    )