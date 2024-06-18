from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Recipe


# form per creare le ricette
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "description",
            "ingredients",
            "instructions",
            "meal_type",
            "cuisine_type",
        ]

        ingredients = forms.CharField(widget=RichTextWidget())
        instructions = forms.CharField(widget=RichTextWidget())

        widget = {
            "description": forms.Textarea(attrs={"rows": 5}),
        }
        labels = {
            "title": "Recipe Title",
            "description": "Description",
            "ingredients": "Ingredients",
            "instructions": "Instructions",
            "meal_type": "Meal Type",
            "cuisine_type": "Cuisine Type",
        }
