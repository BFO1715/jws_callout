from django.shortcuts import render
from django.views import generic
from .models import Request 
from .forms import RequestForm


class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6 


class AddRequest(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'add_request.html'
    #fields = '__all__'