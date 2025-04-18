from django.contrib import admin
from tasks.models import Tasks

# Register your models here.

@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'due_date', 'completed')
    list_filter = ('category', 'completed')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)