from django.db import models

# Create your models here.
class words(models.Model):
    regular_word=models.CharField(max_length=100)
    def __str__(self):
        return f'{self.regular_word}'



