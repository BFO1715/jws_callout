from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Request 
from .forms import RequestForm
from .forms import CommentForm


class RequestList(generic.ListView):
    model = Request
    queryset = Request.objects.order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6 


class RequestDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Request.objects.filter(slug=slug)
        request_obj = get_object_or_404(queryset, slug=slug)
        comments = request_obj.comments.filter(approved=True).order_by("-created_on")
        
        return render(
            request,
            "callout_request.html",
            {
                "request": request,
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
            comment.request = request_obj  # Use request_obj, not request
            comment.save()
        else:
            comment_form = CommentForm(data=request.POST)  # Reuse the existing form instance
        
        return render(
            request,
            "callout_request.html",
            {
                "request": request,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form  # Use the existing form instance
            },
        )

class AddRequest(generic.CreateView):
    model = Request
    form_class = RequestForm
    template_name = 'add_request.html'
  