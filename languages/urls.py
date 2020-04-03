from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register("languages", views.languageView)
router.register("paradigm", views.ParadigmView)
router.register("programmer", views.ProgrammerView)

urlpatterns = [path("", include(router.urls))]
