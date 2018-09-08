from django.contrib import admin
from first_app.models import AccessRecords,Topic,Webpage
from first_app.models import UserProfileInfo, User


# Register your models here.
admin.site.register(AccessRecords)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserProfileInfo)
