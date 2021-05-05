from django.contrib import admin
from . import models 

@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    
    """ Custom User Admin """

    list_display = ("username", "bank_name", "bank_account_num")