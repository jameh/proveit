from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm

def index(request):
    if request.user.is_authenticated():
        context = {"proof_list": [{"get_absolute_url": "lala", "title": "lala"}],
            "username": request.user.username}
        return render(request, 'proveit/index.html', context)
    else:
        context = {"proof_list": [{"get_absolute_url": "lala", "title": "lala"}]}
        return render(request, 'proveit/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("proveit/index.html")
    else:
        form = UserCreationForm()
    return render(request, "proveit/register.html", {
        'form': form,
    })