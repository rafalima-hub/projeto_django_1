# projects\views\register.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from projects.forms import RegisterForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = RegisterForm()

    return render(
        request, 
        'projects/register.html', 
        {'form': form}
    )