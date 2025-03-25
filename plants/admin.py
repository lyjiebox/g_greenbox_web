from django.contrib import admin
from .models import Plant, UserPlant, Comment

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'scientific_name', 'difficulty_level')
    search_fields = ('name', 'scientific_name')
    list_filter = ('difficulty_level', 'light_requirements')

@admin.register(UserPlant)
class UserPlantAdmin(admin.ModelAdmin):
    list_display = ('user', 'plant', 'nickname', 'acquired_date', 'last_watered')
    search_fields = ('user__username', 'plant__name', 'nickname')
    list_filter = ('acquired_date', 'last_watered')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'plant', 'content', 'created_at')
    search_fields = ('user__username', 'plant__name', 'content')
    list_filter = ('created_at',) 