from django.db import models

class Cars(models.Model):
    
    name = models.CharField(max_length=30, default="Indigo")
    cc = models.IntegerField(max_length=6, default=500)
    brand = models.CharField(max_length=30, default="Indian")

    def __str__(self):
     return self.name
    