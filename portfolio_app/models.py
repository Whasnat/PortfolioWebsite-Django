from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    image = models.ImageField(upload_to = 'postfolio_app/images')
    url =   models.URLField(blank=True)
