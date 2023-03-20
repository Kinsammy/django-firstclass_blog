from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    created_at = models.DateTimeField(auto_now_add=True)

    # To string below method will change the object name to string
    def __str__(self):
        return self.title
