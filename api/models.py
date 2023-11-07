from django.db import models


class Rota(models.Model):
    title = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=128, db_index=True, unique=True, null=True)
    description = models.CharField(max_length=1000, null=True)
    tags = models.JSONField(null=True)
    
    
