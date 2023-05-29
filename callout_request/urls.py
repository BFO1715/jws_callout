from . import views
from django.urls import path


urlpatterns = [
    path("", views.RequestList.as_view(), name="home"),
]