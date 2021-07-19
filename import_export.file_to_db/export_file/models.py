from django.db import models

# Create your models here.
class word(models.Model):
    word_list=models.CharField(max_length=100)
    def __str__(self):
        return self.word_list


