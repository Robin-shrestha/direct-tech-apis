from django.db import models

# Create your models here.
class Gallery(models.Model):
    artist = models.CharField(max_length=40, null=True, blank=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Gallery')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"