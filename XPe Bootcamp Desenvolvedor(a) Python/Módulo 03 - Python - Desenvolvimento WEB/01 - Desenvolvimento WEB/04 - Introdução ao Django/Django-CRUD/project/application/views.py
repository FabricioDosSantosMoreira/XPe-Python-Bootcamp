from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render

from application.forms import UserForm
from application.models import User


def index(request: WSGIRequest) -> HttpResponse:

    users = User.objects.all()
    
    context = {'users': users}

    return render(request, 'index.html', context)


def create(request: WSGIRequest) -> HttpResponse:
    if request.method == 'GET':
        form = UserForm()

        context = {'form': form}

        return render(request, 'criar.html', context=context)
    
    else:
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect(index)


def refresh(request: WSGIRequest, user_id: int) -> HttpResponse:
    user = User.objects.get(pk=user_id)

    if request.method == 'POST':
        form = UserForm(data=request.POST, instance=user)
        if form.is_valid():
            form.save()

            return redirect(index)
        
    else:
        form = UserForm(instance=user)

    context = {'form': form}

    return render(request, 'criar.html', context=context)
  

def delete(request: WSGIRequest, user_id: int) -> HttpResponse:
    user = User.objects.get(pk=user_id)

    user.delete()

    return redirect(index)
