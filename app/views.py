from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    context = {
        'data': 'Hello, world. You\'re at the app index.',
    }
    return render(request, 'app/index.html', context)

def logout_view(request):
    logout(request)
    return redirect('index')

def accounts_profile(request):
    return redirect('accounts_detail', request.user.id)

def accounts_detail(request, pk):
    context = {
        'data': 'Hello, world. You\'re at the app accounts detail page.',
    }
    return render(request, 'app/accounts/detail.html', context)


def main(request):
  
  return render(request, 'main.html')

def nawa(request):
  
  return render(request, 'nawa.html')
