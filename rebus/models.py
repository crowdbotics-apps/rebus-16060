from django.conf import settings
from django.db import models


class Categorie(models.Model):
    "Generated Model"
    nom = models.TextField()
    slug = models.SlugField(max_length=50, null=True, blank=True,)


class Lettrebus(models.Model):
    "Generated Model"
    d_creation = models.DateTimeField(auto_now=True,)
    categorie = models.ForeignKey(
        "rebus.Categorie",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="lettrebus_categorie",
    )
    image = models.CharField(max_length=256, null=True, blank=True,)


# Create your models here.
