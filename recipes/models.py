from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField

MEAL_TYPES = (("colazione", "Colazione"), ("pranzo", "Pranzo"), ("cena", "Cena"))

CUISINE_TYPE = (
    ("other", "Other"),
    ("african", "African"),
    ("americana", "Americana"),
    ("asian", "Asian"),
    ("chinese", "Chinese"),
    ("indian", "Indian"),
    ("italian", "Italian"),
)

# Modelli per la creazione, gestione e eliminazione di ricette


class Recipe(models.Model):
    user = models.ForeignKey(User, related_name="recipe_owner", on_delete=models.CASCADE)
    title = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    ingredients = RichTextField(max_length=10000, null=False, blank=False)
    instructions = RichTextField(max_length=10000, null=False, blank=False)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="Colazione")

    favourite = models.ManyToManyField(User, related_name="favourites", blank=True)

    cuisine_type = models.CharField(
        max_length=50, choices=CUISINE_TYPE, default="Other"
    )
    posted_date = models.DateTimeField(
        auto_now=True
    )  # inserire automaticamente la data e ora


# modello per ordinare le ricette
class Meta(models.Model):
    ordering = ["-posted_date"]


def __str__(self):
    return self.title
