from . import views
from django.urls import path
from .views import AddRequest, RequestDetail, EditRequest, DeleteRequest


urlpatterns = [
    path('', views.RequestList.as_view(), name='home'),
    path('add_request/', AddRequest.as_view(), name='add_request'),
    path('<slug:slug>/', views.RequestDetail.as_view(), name='request_detail'),
    path('edit/<slug:slug>/', views.EditRequest.as_view(), name='edit_request'),
    path('delete/<slug:slug>/', views.DeleteRequest.as_view(), name='delete_request'),
]