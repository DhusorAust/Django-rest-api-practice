from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Post_c(models.Model):
    title=models.CharField(max_length=100)
    url=models.URLField()
    poster=models.ForeignKey(User, on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering=['-created']


class Vote(models.Model):
    voter=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post_c, on_delete=models.CASCADE)
        