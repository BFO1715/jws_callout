from django.urls import path
from .views import RequestList, RequestDetail, AddRequest, EditRequest, DeleteRequest

# URL Paths for links
urlpatterns = [
    path('', RequestList.as_view(), name='home'),
    path('add_request/', AddRequest.as_view(), name='add_request'),
    path('<slug:slug>/', RequestDetail.as_view(), name='request_detail'),
    path('edit/<slug:slug>/', EditRequest.as_view(), name='edit_request'),
    path('delete/<slug:slug>/', DeleteRequest.as_view(), name='delete_request'),
]