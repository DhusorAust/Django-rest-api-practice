from django.shortcuts import render


from .models import Post_c

# Create your views here.

from  rest_framework import generics

from .serializers import Post_Serializer_c

class PostList_c(generics.ListCreateAPIView):
    
    
    queryset=Post_c.objects.all()

    serializer_class=Post_Serializer_c
