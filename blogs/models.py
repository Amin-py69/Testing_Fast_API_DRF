from django.db import models
from django.contrib.auth.models import User


class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='user')
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    blogs = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField()
    create = models.DateField()

    def __str__(self):
        return self.text
