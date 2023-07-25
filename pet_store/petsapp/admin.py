from django.contrib import admin
from .models import Pet
from django.utils.html import format_html

class CustomAdmin(admin.ModelAdmin):
    list_display = ('name','species','breed','description','dog_img')
    list_filter = ('gender','species')

    def dog_img(self,obj):
        return format_html('<img src="{}" width="90" height="100" />',obj.image.url)


# Register your models here.

admin.site.register(Pet,CustomAdmin)
admin.site.site_header="Pet Store Admin Panel"
admin.site.site_title="Welcome to Pet Store"
admin.site.index_title="Pet App Admin"
