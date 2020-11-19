from django.contrib import admin
from .models import Gallery, Message, Blog, BlogImages

# Register your models here.
admin.site.register(Gallery)
admin.site.register(Message)
admin.site.register(Blog)
admin.site.register(BlogImages)

