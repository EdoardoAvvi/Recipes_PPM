from django.urls import path
from .views import (
    AddRecipe, Recepies,
    RecipeDetail, DeleteRecipe,
    EditRecipe
)

urlpatterns = [
    path("add/", AddRecipe.as_view(), name="add_recipe"),
    path("", Recepies.as_view(), name="recipes"),
    path("<slug:pk>/", RecipeDetail.as_view(), name="recipe_detail"),
    path("delete/<slug:pk>/", DeleteRecipe.as_view(), name="delete_recipe"),
    path("edit/<slug:pk>/", EditRecipe.as_view(), name="edit_recipe")
]
