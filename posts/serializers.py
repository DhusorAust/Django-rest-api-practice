from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import User


from .models import Post_c


class Post_Serializer_c(serializers.ModelSerializer):

    class Meta:
        model=Post_c

        fields=['id','title','url','poster','created']
            