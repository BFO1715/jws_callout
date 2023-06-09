from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Request model
class Request(models.Model):
    description = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    featured_image = CloudinaryField('image', default='placeholder')
    equipment = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]
    

    def __str__(self):
        return self.description


    def get_absolute_url(self):
        return reverse('home')

# Comment model
class Comment(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=True)

    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"Comment {self.body} by {self.name}"