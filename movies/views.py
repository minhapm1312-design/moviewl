from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

from .models import Movie
from .forms import MovieForm


# ---------------------------
# MOVIE LIST (USER-SPECIFIC)
# ---------------------------
@login_required
def movie_list(request):
    movies = Movie.objects.filter(user=request.user)

    return render(
        request,
        'movies/list.html',
        {'movies': movies}
    )


# ---------------------------
# CREATE MOVIE
# ---------------------------
@login_required
def movie_create(request):

    form = MovieForm(request.POST or None)

    if form.is_valid():
        movie = form.save(commit=False)
        movie.user = request.user
        movie.save()

        return redirect('movie_list')

    return render(
        request,
        'movies/form.html',
        {'form': form}
    )


# ---------------------------
# UPDATE MOVIE
# ---------------------------
@login_required
def movie_update(request, id):

    movie = get_object_or_404(
        Movie,
        id=id,
        user=request.user
    )

    form = MovieForm(request.POST or None, instance=movie)

    if form.is_valid():
        form.save()
        return redirect('movie_list')

    return render(
        request,
        'movies/form.html',
        {'form': form}
    )


# ---------------------------
# DELETE MOVIE
# ---------------------------
@login_required
def movie_delete(request, id):

    movie = get_object_or_404(
        Movie,
        id=id,
        user=request.user
    )

    movie.delete()

    return redirect('movie_list')


# ---------------------------
# REGISTER USER
# ---------------------------
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')

    else:
        form = UserCreationForm()

    return render(
        request,
        'movies/register.html',
        {'form': form}
    )


# ---------------------------
# LOGIN USER
# ---------------------------
def user_login(request):

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movie_list')

    else:
        form = AuthenticationForm()

    return render(
        request,
        'movies/login.html',
        {'form': form}
    )


# ---------------------------
# LOGOUT USER
# ---------------------------
def user_logout(request):
    logout(request)
    return redirect('login')