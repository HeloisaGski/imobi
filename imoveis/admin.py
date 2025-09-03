from django.contrib import admin
from .models import Property, Contact

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'state', 'is_available', 'created_at')
    list_filter = ('is_available', 'city', 'state')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zip_code')
    ordering = ('-created_at',)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property', 'created_at')
    list_filter = ('created_at', 'property')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)

# Register your models here.
