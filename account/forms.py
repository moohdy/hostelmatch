from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class UserRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(help_text='A minimum of 8 characters', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','password1','password2','first_name','last_name','profile_picture','phone_number','address','date_of_birth')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        #user.active = False #send confirmation email first
        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','phone_number','password1','password2','first_name','last_name','profile_picture','address','date_of_birth')


    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password','first_name','last_name', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

'''
from django.contrib.auth.models import User
from .models import Profile#, Landlord, Roomie

class UserRegistrationForm(forms.ModelForm):
    
    #this form is a model form for login and rely on django's User model. the password field extends the user model

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
    
    
    def unique_email(self):
        cd = self.cleaned_data
        if cd['email']
            raise forms.ValidationError('Email address is already in use')
        return cd['email']
    

class ProfileCreationForm(forms.ModelForm):

    #a model form that rely on the profile model from model.py. this form is used for editing the data in the model which is
    #empty or blank on creation
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
    
    #a model form that rely on the profile model from model.py. this form is used for editing the data in the model which is
   # empty or blank on creation
    class Meta:
        model = Profile
        fields = ('photo','contact','date_of_birth','location')
        widgets ={
            "contact":forms.TextInput(attrs={'label':'Phone number','onblur':'validateContact(this.value)', 'id':'contact','name':'contact'}),
            "date_of_birth":forms.DateInput(attrs={'label':'date_of_birth','id':'dob','name':'dob'}),
            "location":forms.TextInput(attrs={'label':'Location','id':'location','name':'location'}),
            "photo":forms.FileInput(attrs={'class':'form-control', 'id':'photo', 'name':'photo'}),
        }
'''