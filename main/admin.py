from django.contrib import admin
from main.models import Animals


@admin.register(Animals)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','age','description',)
    readline_fields = ('name','age',)
    list_filter = ('name',)
    search_fields = ('name','age','description',)
