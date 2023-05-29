from django.shortcuts import render
from django.views import generic 
from .models import Request 


class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6 

