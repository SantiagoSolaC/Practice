from django.db import models

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(null=True, max_length=30)