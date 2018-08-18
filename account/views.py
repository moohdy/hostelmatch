from django.shortcuts import render, get_object_or_404
#from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm, SearchForm, LandlordForm, RoomieForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
#from .models import Profile, Landlord, Roomie
#from hostel.models import Hostel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
#from haystack.query import SearchQuerySet


#a view for retriving a user dashboard profile
@login_required
def dashboard(request):
    context = {'section':'dashboard'}
    return render (request, 'account/profile.html',context)



