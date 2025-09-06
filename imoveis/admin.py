from django.contrib import admin
from .models import Property, Contact, NewsletterSignup, Favorite

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'city', 'rental_type', 'is_available', 'created_at')
    list_filter = ('rental_type', 'is_available', 'city', 'state')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zip_code')
    ordering = ('-created_at',)
    fields = ('title', 'description', 'price', 'address', 'city', 'state', 'zip_code', 'bedrooms', 'bathrooms', 'area', 'image', 'whatsapp_number', 'rental_type', 'is_available')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'property', 'created_at')
    list_filter = ('created_at', 'property')
    search_fields = ('name', 'email', 'phone', 'message')
    readonly_fields = ('created_at',)

@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_at')
    search_fields = ('email',)
    readonly_fields = ('created_at',)

# Register your models here.
