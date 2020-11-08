from django.db import models

# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=30)
    network = models.CharField(max_length=30)
    release = models.DateField(auto_now=False, auto_now_add=False, null=True)
    desc = models.TextField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    