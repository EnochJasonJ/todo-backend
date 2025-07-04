from django.contrib import admin
from .models import TaskModel

# Register your models here.
class TaskModelAdmin(admin.ModelAdmin):
    list_display = ('title','user','is_archived','created_at')
    list_filter = ('user','is_archived')
    search_fields = ('title','user__username')

admin.site.register(TaskModel, TaskModelAdmin)
