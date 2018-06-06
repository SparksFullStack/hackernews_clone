from django.db import models

# here we created the model of a Link to store in the database
class Link(models.Model):
    url = models.URLField()
    description = models.TextField(blank=True)