from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CategorieViewSet, LettrebusViewSet

router = DefaultRouter()
router.register("categorie", CategorieViewSet)
router.register("lettrebus", LettrebusViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
