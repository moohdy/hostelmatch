from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'last_name', 'first_name', 'phone_number', 'reg_date','active', 'admin')
    list_filter = ('admin','reg_date',)
    fieldsets = (
        ('Login info', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('last_name','first_name', 'phone_number', 'email', 'profile_picture', 'address',)}),
        ('Permissions', {'fields': ('active', 'staff','admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('User info', {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'phone_number','first_name','last_name','profile_picture','address','date_of_birth','active','staff','admin',)}
        ),
    )
    search_fields = ('email','phone_number',)
    ordering = ('-reg_date','email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)

'''
from .models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
#from homes.admin import HouseInline



class ProfileAdmin(admin.ModelAdmin):
    #admin interface for profile model
    list_display = ('user', 'photo','contact','date_of_birth', 'location','reg_date' )
    date_hierarchy = 'reg_date'
    
admin.site.register(Profile, ProfileAdmin)


class ProfileInline(admin.StackedInline):
    #making the profile model an inline model for the user model on the admin interface 
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    
class UserAdmin(BaseUserAdmin):
    #registring the profile model as inline model to the user model in admin interface
    inlines = (ProfileInline,)
    
#Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)


'''