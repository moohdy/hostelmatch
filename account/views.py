from django.shortcuts import render, get_object_or_404
from .forms import UserRegistrationForm ,LandlordRegistrationForm, RoomieRegistrationForm# UserEditForm, ProfileEditForm#, SearchForm 
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, get_user_model
#from .models import Profile#, Landlord, Roomie
#from hostel.models import Hostel
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.contrib.auth.models import User
#from haystack.query import SearchQuerySet
User = get_user_model()

#a view for retriving a user dashboard profile
@login_required
def dashboard(request):
    #a view for retriving a user profile from the database
    #user = get_object_or_404(User, email=email)
    '''
    #a view for haystack search form in homes application
    #a view for the homepage that list houses, a registration form etc
    if 'query' in request.GET:
        searchform = SearchForm(request.GET)
        if searchform.is_valid():
            cd = searchform.cleaned_data
            results = SearchQuerySet().models(House).filter(content=cd['query']).load_all()
            # count total results
            total_results = results.count()
            context = {'searchform':searchform, 'cd':cd, 'results':results, 'total_results':total_results}
            return render(request, 'registration/homessearch.html', context)
    else:
        searchform = SearchForm()
    '''
    context = {'section':'dashboard'}
    return render (request, 'account/profile.html',context)

#a view for registring users through a form

def register(request):
    if request.method == 'POST':
        # The form was posted
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            # Create user object but don't save to database yet
            #new_user = register_form.save(commit=False)
            #set the choosen password
            #new_user.set_password(register_form.cleaned_data['password'])
            # Save the user to the database
            #new_user.save()
            # Create the unpopulated user profile
            #profile = Profile.objects.create(user=new_user)
            #new_user_profile.save()
            register_form.save()
            #context = {'new_user':new_user}
            return render(request,'account/register_done.html')#, context)   
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

@login_required
def register_landlord(request):
    if request.method == 'POST':
        register_landlord = LandlordRegistrationForm(request.POST)
        if register_landlord.is_valid():
            new_landlord = register_landlord.save(commit=False)
            new_landlord.user = request.user
            new_landlord.save()
            # Create the unpopulated user profile
            #profile = Profile.objects.create(user=new_user)
            #new_user_profile.save()
            #register_landlord.save()
            return render(request, 'account/registerlandlord_done.html')
    else:
        register_landlord = LandlordRegistrationForm()
    context = {'register_landlord':register_landlord}
    return render(request, 'account/register_landlord.html', context)

@login_required
def register_roomie(request):
    if request.method == 'POST':
        register_roomie = RoomieRegistrationForm(request.POST, request.FILES)
        print('test')
        print(register_roomie.errors)
        if register_roomie.is_valid():
            print('testim')
            print('testim')
            new_roomie = register_roomie.save(commit=False)
            print('testim')
            new_roomie.user = request.user
            new_roomie.save()
            return render(request, 'account/registerroomie_done.html')
    else:
        register_roomie = RoomieRegistrationForm()
    context = {'register_roomie':register_roomie}
    return render(request, 'account/register_roomie.html', context)