from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Request 
from .forms import RequestForm
from .forms import CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

# Request list view
class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

# Request list detail
class RequestDetail(generic.View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Request.objects.filter(slug=slug)
        request_obj = get_object_or_404(queryset, slug=slug)
        comments = request_obj.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "callout_request.html",
            {
                "request_obj": request_obj,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm()
            },
        )


    def post(self, request, slug, *args, **kwargs):
        queryset = Request.objects.filter(slug=slug)
        request_obj = get_object_or_404(queryset, slug=slug)
        comments = request_obj.comments.filter(approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.request = request_obj  
            comment.save()
        else:
            comment_form = CommentForm(data=request.POST)  

        return render(
            request,
            "callout_request.html",
            {
                "request_obj": request_obj,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form  
            },
        )

# Create request view
class AddRequest(LoginRequiredMixin, generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'add_request.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

# Edit request view
class EditRequest(LoginRequiredMixin, generic.UpdateView):
    model = Request
    template_name = 'edit_request.html'
    form_class = RequestForm

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

# Delete request view
class DeleteRequest(LoginRequiredMixin, generic.DeleteView):
    model = Request
    template_name = 'delete_request.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)