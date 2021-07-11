from django.shortcuts import render, redirect
from .forms import UserForm



def subscribe(request):
    return render(request, 'subscribe.html', {})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'register.html', {'form': form})


