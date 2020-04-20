from rest_framework import serializers
from rebus.models import Categorie, Lettrebus


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = "__all__"


class LettrebusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lettrebus
        fields = "__all__"
