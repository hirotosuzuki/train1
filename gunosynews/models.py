from django.db import models

# Create your models here.


class Gunosy(models.Model):
    article_title = models.CharField(max_length=100)
    article_category = models.CharField(max_length=10)
