from django.contrib import admin
from core.models import *
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','subject','message','created_at')
    list_filter = ('name',)
    search_fields = ('name',)

admin.site.register(HeaderImage)
