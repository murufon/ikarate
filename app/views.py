from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from .decorators import twitter_login_required
from .models import TwitterAuthToken, TwitterUser
from .authorization import create_update_user_from_twitter, check_token_still_valid
from .twitter_api import TwitterAPI

# Create your views here.
# @login_required
# @twitter_login_required
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

def sample(request):
    messages = list()
    messages.append({
        "tags": "success",
        "text": "募集を作成しました"
    })
    context = {
        'messages': messages,
        'title': 'サンプルページ'    
    }
    return render(request, 'app/sample/index.html', context)

def boshuuran(request):
  
  return render(request, 'boshuuran.html')

def boshuu(request):
  
  return render(request, 'boshuu.html')


def twitter_login(request):
    twitter_api = TwitterAPI()
    url, oauth_token, oauth_token_secret = twitter_api.twitter_login()
    if url is None or url == '':
        messages.add_message(request, messages.ERROR, 'Unable to login. Please try again.')
        return render(request, 'app/error_page.html')
    else:
        twitter_auth_token = TwitterAuthToken.objects.filter(oauth_token=oauth_token).first()
        if twitter_auth_token is None:
            twitter_auth_token = TwitterAuthToken(oauth_token=oauth_token, oauth_token_secret=oauth_token_secret)
            twitter_auth_token.save()
        else:
            twitter_auth_token.oauth_token_secret = oauth_token_secret
            twitter_auth_token.save()
        return redirect(url)


def twitter_callback(request):
    if 'denied' in request.GET:
        messages.add_message(request, messages.ERROR, 'Unable to login or login canceled. Please try again.')
        return render(request, 'app/error_page.html')
    twitter_api = TwitterAPI()
    oauth_verifier = request.GET.get('oauth_verifier')
    oauth_token = request.GET.get('oauth_token')
    twitter_auth_token = TwitterAuthToken.objects.filter(oauth_token=oauth_token).first()
    if twitter_auth_token is not None:
        access_token, access_token_secret = twitter_api.twitter_callback(oauth_verifier, oauth_token, twitter_auth_token.oauth_token_secret)
        if access_token is not None and access_token_secret is not None:
            twitter_auth_token.oauth_token = access_token
            twitter_auth_token.oauth_token_secret = access_token_secret
            twitter_auth_token.save()
            # Create user
            info = twitter_api.get_me(access_token, access_token_secret)
            if info is not None:
                twitter_user_new = TwitterUser(twitter_id=info[0]['id'], screen_name=info[0]['username'],
                                               name=info[0]['name'], profile_image_url=info[0]['profile_image_url'])
                twitter_user_new.twitter_oauth_token = twitter_auth_token
                user, twitter_user = create_update_user_from_twitter(twitter_user_new)
                if user is not None:
                    login(request, user)
                    return redirect('index')
            else:
                messages.add_message(request, messages.ERROR, 'Unable to get profile details. Please try again.')
                return render(request, 'app/error_page.html')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to get access token. Please try again.')
            return render(request, 'app/error_page.html')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to retrieve access token. Please try again.')
        return render(request, 'app/error_page.html')


# @login_required
# @twitter_login_required
# def index(request):
#     return render(request, 'app/index.html')


@login_required
def twitter_logout(request):
    logout(request)
    return redirect('index')