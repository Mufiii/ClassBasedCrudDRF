from django.contrib import admin
from api.models import Football

# Register your models here.


@admin.register(Football)
class FootballAdmin(admin.ModelAdmin):
    list_display = ['id','team','player','jersey_no']