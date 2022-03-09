from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField()
    images = models.ImageField(upload_to="Books/%y/%m/", help_text="Kitobni rasmini yuklang")

    def __str__(self):
        return self.title

