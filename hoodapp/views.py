from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import BusinessForm, ProfileForm, HoodForm, PostForm
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood, Business, Post 


# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')
