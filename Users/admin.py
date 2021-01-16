from django.contrib import admin
from django.contrib.sessions.models import Session
from .models import CustomUser,Student,Sheet,worksheet, Alum_Detail

admin.site.register(CustomUser)
admin.site.register(Session)
admin.site.register(Sheet)
admin.site.register(Student)
admin.site.register(Alum_Detail)
admin.site.register(worksheet)
# Register your models here.
