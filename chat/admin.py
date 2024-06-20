from django.contrib import admin

from .models import Chat, Message
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    field = ('chat', 'text', 'created_at', 'author', 'receiver')
    list_display = ('text', 'created_at', 'author', 'receiver')
    search_fields = ('text', )

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)