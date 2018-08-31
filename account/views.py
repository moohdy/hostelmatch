from django.shortcuts import render, get_object_or_404
from .forms import UserRegistrationForm , UserEditForm, ProfileEditForm#, SearchForm, LandlordForm, RoomieForm
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from .models import Profile#, Landlord, Roomie
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

#a view for registring users through a form
def register(request):
    if request.method == 'POST':
        # The form was posted
        register_form = UserRegistrationForm(request.POST, request.FILES)
        if register_form.is_valid():
            # Create user object but don't save to database yet
            new_user = register_form.save(commit=False)
            #set the choosen password
            new_user.set_password(register_form.cleaned_data['password'])
            # Save the user to the database
            new_user.save()
            # Create the unpopulated user profile
            profile = Profile.objects.create(user=new_user)
            context = {'new_user':new_user}
            return render(request,'account/register_done.html', context)   
    else:
        register_form = UserRegistrationForm()
    context = { 'register_form':register_form}
    return render(request,'account/register.html', context)


@login_required
def edit_profile(request):
    #a view for editing user profile data saved to the database
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    context = {'profile_form':profile_form, 'user_form':user_form}
    return render(request,'account/edit_profile.html', context)