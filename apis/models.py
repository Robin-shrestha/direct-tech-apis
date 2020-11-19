from django.db import models

# Create your models here.
class Gallery(models.Model):
    artist = models.CharField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='Gallery')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"


class Message(models.Model): 
    subject = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField()
    email = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=60)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}: {self.subject}, date added: {self.date_added}"

class Blog(models.Model):
    blog_title = models.CharField(max_length=255)
    blog_body = models.TextField()
    author = models.CharField(max_length=63)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.blog_title}| created on: {self.date_added}"

class BlogImages(models.Model):
    images = models.ImageField(upload_to='blog/%Y/%m/%d/')
    blog_post = models.ForeignKey(Blog, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return f"image from {self.blog_post}"