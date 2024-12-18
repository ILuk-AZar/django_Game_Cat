from django.shortcuts import render, redirect
from .models import Game, Genre
from .forms import GameForm
from django.db.models import Q


def game_list(request):
    games = Game.objects.all()
    search_param = request.GET.get('search_param')
    query = request.GET.get('q')
    min_value = request.GET.get('min_value')
    max_value = request.GET.get('max_value')

    if search_param and query:
        if search_param == 'title':
            games = games.filter(title__icontains=query)
        elif search_param == 'developer':
            games = games.filter(developer__icontains=query)
        elif search_param == 'publisher':
            games = games.filter(publisher__icontains=query)
        elif search_param == 'genre':
            games = games.filter(genre__name__icontains=query)
        elif search_param == 'release_year':
            if min_value and max_value:
                games = games.filter(release_year__range=(min_value, max_value))
        elif search_param == 'price':
            if min_value and max_value:
                games = games.filter(price__range=(min_value, max_value))

    return render(request, 'games/game_list.html', {'games': games})
def add_game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm()
    return render(request, 'games/add_game.html', {'form': form})