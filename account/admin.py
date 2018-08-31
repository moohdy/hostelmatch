from django.contrib import admin
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


