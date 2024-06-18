from django.urls import path
from .views import Profiles, EditProfile

from . import views

app_name = 'profiles'

urlpatterns = [
    path("user/<slug:pk>/", Profiles.as_view(), name="profile"),
    path("edit/<slug:pk>/", EditProfile.as_view(), name="edit_profile"),
    path("fav/<int:id>/", views.favourite_add, name="favourite_add"),
    path("favourite/", views.favourite_list, name="favourite_list"),
]
