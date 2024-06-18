from django.views.generic import(
    CreateView, ListView,
    DeleteView, DetailView,
    UpdateView
)

# per fare il check se l'utente è loggato
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

#per gestire operazioni complesse su tabelle con meno codice
from django.db.models import Q

from .models import Recipe
from .forms import RecipeForm


# lista delle ricette
class Recepies(ListView):
    template_name = "recipes/recipes.html"
    model = Recipe
    context_object_name = "recipes"

    def get_queryset(self, **kwargs):
        query = self.request.GET.get("query")
        if query:
            #fà il check se la parola cercata è in uno dei campi indicati sotto
            recipes = self.model.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(ingredients__icontains=query) |
                Q(meal_type__icontains=query) |
                Q(cuisine_type__icontains=query)
            )
        else:
            #se la ricerca è vuota ritorna tutte le ricette
            recipes = self.model.objects.all()
        return recipes


# classe per reperire i dettagli della ricetta cliccata
class RecipeDetail(DetailView):
    template_name = "recipes/recipe_detail.html"
    model = Recipe
    context_object_name = "recipe"



# classe per aggiungere ricette
class AddRecipe(LoginRequiredMixin, CreateView):
    template_name = "recipes/add_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    # funz per impostare come autore direttamente chi è loggato
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddRecipe, self).form_valid(form)

#modifica di una ricetta, simile alla cancellazione
#controllando che sia l'utente giusto e possa farlo


class EditRecipe(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "recipes/edit_recipe.html"
    model = Recipe
    form_class = RecipeForm
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user

#classe per l'eleminazione di ricette
#il LoginReq..Mixin serve per rendirizzare se l'utente non si è loggato
#mentre lo UserPass...Mixin per capire se la ricetta è dell'utente che si è loggato o meno
#dopodiché si può procedere alla cancellazione

class DeleteRecipe(LoginRequiredMixin,UserPassesTestMixin ,DeleteView):
    model = Recipe
    success_url = "/recipes/"

    def test_func(self):
        return self.request.user == self.get_object().user
