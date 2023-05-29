from . import views
from django.urls import path
from .views import AddRequest


urlpatterns = [
    path('', views.RequestList.as_view(), name='home'),
    path('add_request/', AddRequest.as_view(), name='add_request'),
    path('<slug:slug>/', views.RequestDetail.as_view(), name='request_detail'),
]