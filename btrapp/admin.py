from django.contrib import admin

from btrapp.models import CaseManagement,UserProfile

# Register your models here.

admin.site.register(CaseManagement)
admin.site.register(UserProfile)