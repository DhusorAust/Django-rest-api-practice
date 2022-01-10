from django.contrib import admin

# Register your models here.

from .models import Post_c,Vote


admin.site.register(Post_c)
admin.site.register(Vote)


