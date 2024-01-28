from django.db import models

# Create your models here.
class Toy(models.Model):
    name = models.CharField(max_length=100)
    age_recommended = models.IntegerField()
    description = models.TextField(null = True, blank = True)
    is_outdoor = models.BooleanField(null = True, blank = True)

    def __str__(self):
        return self.name