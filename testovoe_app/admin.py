from django.contrib import admin
from .models import Request

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_name', 'phone', 'email', 'status', 'subject', 'created_at')
    search_fields = ('client_name', 'phone', 'status')
    list_filter = ('status', 'created_at')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
