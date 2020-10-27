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
    subject = models.CharField(max_length=250)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    checked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name}: {self.subject}, date added: {self.date_added}"