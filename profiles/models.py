from django.db import models
from djrichtextfield.models import RichTextField

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    bio = RichTextField(max_length=2500, null=True, blank=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
