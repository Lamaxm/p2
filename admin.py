from django.contrib import admin
from .models import List

class ListrAdmin(admin.ModelAdmin):
    list_filter = ['title']
admin.site.register(List, ListrAdmin)
