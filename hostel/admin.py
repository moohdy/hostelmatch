from django.contrib import admin
from .models import Hostel

class HostelInline(admin.StackedInline):
    model = Hostel    

class HostelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'address', 'image1', 'image2', 'image3', 'image4', 'image5',
                    'created', 'description','vacant','price']
    list_filter = ['created']
    prepopulated_fields = {'slug': ('title',)}
    #raw_id_fields = ['landlord']
        
admin.site.register(Hostel, HostelAdmin)
