from django.contrib import admin
from .models import EmailTemplate

@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'updated_at', 'created_at')
    list_filter = ('updated_at',)
    search_fields = ('title', 'body')