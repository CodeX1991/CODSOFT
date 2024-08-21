from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import UserForm
import random
from .models import User, Game


def start_game(request):
    """Start the game"""
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            request.session['username'] = user.username
            return redirect('play_game')
    else:
        form = UserForm()
    return render(request, 'game/start_game.html', {'form': form})

def play_game(request):
    """Play game"""
    if request.method == 'POST':
        player_choice = request.POST.get('choice')
        if player_choice not in ['rock', 'paper', 'scissors']:
            return HttpResponse("Invalid choice", status=400)
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        return redirect('game_result', player_choice=player_choice, computer_choice=computer_choice)
    return render(request, 'game/game_page.html')

def game_result(request, player_choice, computer_choice):
    """Diaplay result"""
    if player_choice == computer_choice:
        result = 'It is a tie'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        result = 'wins'
    else:
        result = 'loses'
    
    username = request.session.get('username')
    if not username:
        return redirect('start_game')
    
    user = get_object_or_404(User, username=username)
    game = Game(player=user, player_choice=player_choice, computer_choice=computer_choice, result=result)
    game.save()

    return render(request, 'game/game_result.html', {
        'username': user.username,
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
    })

def end_game(request):
    """End the game"""
    username = request.session.get('username')
    if not username:
        return redirect('start_game')
    
    user = get_object_or_404(User, username=username)
    games = Game.objects.filter(player=user).order_by('-timestamp')

    copy_game = list(games)
    user.delete()

    return render(request, 'game/end_game.html', {'games': copy_game})