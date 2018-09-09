from django import forms
from django.contrib.auth.models import User
from .models import Profile#, Landlord, Roomie

class UserRegistrationForm(forms.ModelForm):
    '''
    this form is a model form for login and rely on django's User model. the password field extends the user model
    '''
    password = forms.CharField(label='Password',help_text='A minimum of 8 characters',widget=forms.PasswordInput (attrs=
                {'class':'form-control','placeholder':'Password','id':'password','name':'password','required':True}))
    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput(attrs={'class':'form-control',
                'placeholder':'Confirm Password','id':'password2','name':'password2','required':True}))
    
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username','password','password2','email')
        widgets ={
            "first_name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name', 'id':'firstname',
                'name':'first_name','required':True}),
            "last_name":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Surname','id':'lastname',
                'name':'last_name','required':True}),
            "username":forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username','id':'username',
                'name':'username','required':True}),
            "email":forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email address','id':'email',
                'name':'email','required':True}), 
        }
        
    
    
    def clean_password2(self):
        #a validation on the userregistration form from the user model. it validates that both password1 and password2 match
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Your Passwords didn\'t match. Try again')
        return cd['password2']
    
    '''
    def unique_email(self):
        cd = self.cleaned_data
        if cd['email']
            raise forms.ValidationError('Email address is already in use')
        return cd['email']
    '''

class ProfileCreationForm(forms.ModelForm):
    '''
    a model form that rely on the profile model from model.py. this form is used for editing the data in the model which is
    empty or blank on creation
    '''
    class Meta:
        model = Profile
        fields = ('photo','contact','date_of_birth','location')
        widgets ={
            "contact":forms.TextInput(attrs={'label':'Phone number', 'id':'contact','name':'contact'}),
            "date_of_birth":forms.DateInput(attrs={'label':'date_of_birth','id':'dob','name':'dob'}),
            "location":forms.TextInput(attrs={'label':'Location','id':'location','name':'location'}),
            "photo":forms.FileInput(attrs={'class':'form-control', 'id':'photo', 'name':'photo'}),
        }
        

class UserEditForm(forms.ModelForm):
    #a model form that rely on the user model. this form is used to edit the initial userregistration form data listed
    class Meta:
        model = User
        fields = ('first_name', 'last_name','username', 'email')
        widgets ={
            "first_name":forms.TextInput(attrs={'class':'form-control', 'id':'firstname',
                'name':'first_name','required':True}),
            "last_name":forms.TextInput(attrs={'class':'form-control','id':'lastname',
                'name':'last_name','required':True}),
            "username":forms.TextInput(attrs={'class':'form-control', 'id':'username',
                'name':'username','required':True}),
            "email":forms.EmailInput(attrs={'class':'form-control','id':'email',
                'name':'email','required':True}), 
        }


class ProfileEditForm(forms.ModelForm):
    '''
    a model form that rely on the profile model from model.py. this form is used for editing the data in the model which is
    empty or blank on creation
    '''
    class Meta:
        model = Profile
        fields = ('photo','contact','date_of_birth','location')
        widgets ={
            "contact":forms.TextInput(attrs={'label':'Phone number','onblur':'validateContact(this.value)', 'id':'contact','name':'contact'}),
            "date_of_birth":forms.DateInput(attrs={'label':'date_of_birth','id':'dob','name':'dob'}),
            "location":forms.TextInput(attrs={'label':'Location','id':'location','name':'location'}),
            "photo":forms.FileInput(attrs={'class':'form-control', 'id':'photo', 'name':'photo'}),
        }
        