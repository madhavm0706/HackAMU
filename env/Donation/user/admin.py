from django.contrib import admin
from .models import User, Donation_list, UserUpdate
# Register your models here.


admin.site.register(User)
admin.site.register(Donation_list)
admin.site.register(UserUpdate)