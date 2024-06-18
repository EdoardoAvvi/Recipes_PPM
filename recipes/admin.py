from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "instructions",
        "ingredients",
        "meal_type",
    )
    # per filtrare dal pannello di admin
    list_filter = ("meal_type",)
