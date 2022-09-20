from django.contrib import admin

from .models import Customer, User

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     model = User
admin.site.register(User)
admin.site.register(Customer)
    