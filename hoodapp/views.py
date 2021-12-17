from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import BusinessForm, ProfileForm, HoodForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Business, Post 


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')


def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)
    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {'form': form})
