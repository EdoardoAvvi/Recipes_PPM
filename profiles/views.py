from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

from recipes.models import Recipe
from .forms import ProfileForm
from .models import Profile

@ login_required
def favourite_list(request):
    new = Recipe.favourite.filter(favourites=request.user)
    return render(request,
                  'profiles/favourite.html',
                  {'new': new})

@login_required
def favourite_add(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    if recipe.favourite.filter(id=request.user.id).exists():
        recipe.favourite.remove(request.user)
    else:
        recipe.favourite.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])



class Profiles(TemplateView):
    template_name = "profiles/profile.html"

    # vogliamo poter vedere qualsiasi profilo non solo il nostro
    def get_context_data(self, **kwargs):
        profile = Profile.objects.get(user=self.kwargs["pk"])
        contex = {
            "profile": profile,
            "form": ProfileForm(instance=profile),
        }
        return contex


class EditProfile(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ProfileForm
    model = Profile

    def form_valid(self, form):
        self.success_url = f'/profiles/user/{self.kwargs["pk"]}'
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().user
